import sys, os, subprocess, commands
import logging

class ent_env:

	# ========================================================
	# 	SAM Server Testing Parameters
	# ========================================================

        prior_env="Library"
        default_org="ACME_Corporation"
	default_env="env1"
	default_provider="Red Hat"
	default_provider_repo_url="https://cdn.redhat.com"
	default_manifest="default-manifest.zip"

	username1ss="sam_test_1"
	password1ss="redhat"
	email1="sam_test_1@localhost"
	org1="test_org1"
	env1="test_env1"
	keyname1="test_key1"
	systemname1="system_1"

        password2ss="localhost"
        email2="sam_test_1@redhat.com"
        env2="test_env100"
        keyname2="test_key2"
	systemname2="system_2"

	manifest1="hss-qe-sam20111213.zip"
	manifest1_product1="Red Hat Enterprise Linux Server"
	manifest1_product2="Red Hat Enterprise Linux High Availability for RHEL Server"
	manifest2="hss-qe-sam20111213-update1-remove.zip"
	manifest3="hss-qe-sam20111213-update2-add.zip"
	specific_manifest="rhel6.2-sam-htb.zip"
