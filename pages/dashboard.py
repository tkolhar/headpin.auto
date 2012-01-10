#!/usr/bin/env python

class Dashboard(Base):
    _dropbutton_locator = (By.CSS_SELECTOR, '.dropbutton span')
    _dashboard_subscriptions_locator = (By.CSS_SELECTOR, '.dash #dashboard_subscriptions')
    _dashboard_nofications_locator = (By.ID, 'dashboard_notifications')
    
    