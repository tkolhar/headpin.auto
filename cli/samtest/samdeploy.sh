#! /bin/bash
###
# script for SAM deployment automation
##

function p_date() {
    date +"%F %T"
}

function d_echo() {
    echo $(p_date)" $1"
}

#SAM Deployment Begin
d_echo "############################################"
d_echo "## SAM Deployment"
d_echo "############################################"

MACHINENAME="samserv.redhat.com"

#Step1: Open port 443, 8443 and 8088 for HTTPS connections to Katello.
FILE=/etc/sysconfig/iptables
sed -i '/-A INPUT -j REJECT --reject-with icmp-host-prohibited/i\-A INPUT -p tcp -m state --state NEW -m tcp --dport 443 -j ACCEPT\n-A INPUT -p tcp -m state --state NEW -m tcp --dport 8443 -j ACCEPT\n-A INPUT -p tcp -m state --state NEW -m tcp --dport 8088 -j ACCEPT' $FILE
cmd="service iptables restart"
echo $cmd
eval $cmd
#Check opened ports
iptables=`service iptables status`
if [ -z "$(echo $iptables|grep 'dpt:443')" ] || [ -z "$(echo $iptables|grep 'dpt:8443')" ] || [ -z "$(echo $iptables|grep 'dpt:8088')" ]
then
    echo "Open port 443, 8443 and 8088 FAIL!!!"
fi

#Step2: Configure repos
#Step2-1: Enable optional repo
sed -i 's/^ *hostname *=.*/hostname = subscription.rhn.stage.redhat.com/' /etc/rhsm/rhsm.conf
eval "subscription-manager clean"
cmd="subscription-manager register --username=stage_test_12 --password=redhat"
echo $cmd
eval $cmd
tmp=$(mktemp)
cmd="subscription-manager list --available | tee $tmp"
echo $cmd
eval $cmd
pool_id=$(grep --max-count=1 -A 1 RH0103708 $tmp | awk -F":" '/PoolId/{print $2;}' | sed 's/^[ \t]*//;s/[ \t]*$//')
if [ $pool_id'X' = 'X' ]
then
    echo "no SKU=RH0103708 available. To confirm, run subscription-manager list --available" && fail
else
    cmd="subscription-manager subscribe --pool=$pool_id"
    echo "$cmd"
    eval $cmd
fi
cmd="yum repolist"
echo $cmd
eval $cmd
line=$(($(grep -n "^\[rhel-6-server-optional-rpms\]" /etc/yum.repos.d/redhat.repo | awk -F":" '{print $1}')+3))
sed -i "$line s/0/1/" /etc/yum.repos.d/redhat.repo

#Step2-2: Add SAM repo
baseurl=$1
echo -e "[sam]\\nname = sam\\nbaseurl = $baseurl\\nenabled = 1\\ngpgcheck = 0" > /etc/yum.repos.d/sam.repo
cmd="yum repolist"
echo $cmd
repolist=$(eval $cmd)
echo $repolist
#Check enabled repos
if [ -z "$(echo $repolist|grep rhel-6-server-optional-rpms)" ] || [ -z "$(echo $repolist|grep rhel-6-server-rpms)" ] || [ -z "$(echo $repolist|grep sam)" ] || [ $(repoquery -a --repoid=rhel-6-server-optional-rpms|wc -l) == 0 ] || [ $(repoquery -a --repoid=rhel-6-server-rpms|wc -l) == 0 ] || [ $(repoquery -a --repoid=sam|wc -l) == 0 ]
then
    echo "repos are not configured successfully!!!"
fi

#Step3: Set hostname and add it to /etc/hosts
cmd="hostname $MACHINENAME"
echo $cmd
eval $cmd
HOSTNAME=$(hostname)
IP=$(ifconfig |sed -n 's/inet addr:\([0-9\.]*\).*/\1/p'|awk "NR==1")
echo "$IP $HOSTNAME" >> /etc/hosts
sed -i "s/^ *HOSTNAME*=.*/HOSTNAME=$MACHINENAME/" /etc/sysconfig/network

#Step4: Install katello-headpin-all
cmd="yum install -y katello-headpin-all"
echo $cmd
tmp=$(mktemp)
eval $cmd|tee tmp
#Check installation result
grep "Complete\!" tmp
right=$?
grep "Error:" tmp
wrong=$?
if [ $right -eq 0 ] && [ $wrong -ne 0 ]
then
    echo "Install katello-headpin-all PASS!!!"
else
    echo "Install katello-headpin-all FAIL!!!"
fi
rm -f tmp

#Step5: Configure katello to headpin
cmd="katello-configure --deployment=headpin"
echo $cmd
eval $cmd
#Check configuration result
if [ $? -ne 0 ]
then
    echo "katello configuration FAIL!!!"
else
    echo "katello configuration PASS!!!"
fi
sleep 120s

#Create an environment to default org
cmd="headpin -u admin -p admin environment create --org=ACME_Corporation --name=env1 --prior=Library"
echo $cmd
env=$(eval $cmd)
#Check env creating result
if [ -z "$(echo $env|grep 'Successfully created environment \[ env1 \]')" ]
then
    echo "Creating environment FAIL!!!"
fi
#Import a manifest to default org
filepath=$2
cmd="headpin -u admin -p admin provider import_manifest --org=ACME_Corporation --name='Red Hat' --file=$2"
echo $cmd
manifest=$(eval $cmd)
#Check import manifest result
if [ -z "$(echo $manifest|grep 'Manifest imported')" ]
then
    echo "Importing manifest FAIL!!!"
fi

#SAM Deployment End
cmd="subscription-manager unregister"
echo $cmd
eval $cmd
d_echo "############################################"
d_echo "## SAM Deployment finished"
d_echo "############################################"
