import datetime
import json
import logging
import pytz

from flask import current_app as app
from flask_babel import lazy_gettext as _
from typing import List
from cryptoadvance.specter.specter_error import SpecterError

from cryptoadvance.specter.user import User

from cryptoadvance.specter.services.service import Service, devstatus_alpha
from cryptoadvance.specter.addresslist import Address
from cryptoadvance.specter.wallet import Wallet

logger = logging.getLogger(__name__)


class JmfService(Service):
    id = "jmf"
    name = "Joinmarket GUI"
    icon = "jmf/img/joinmarket.png"
    logo = "jmf/img/joinmarket.png"
    desc = "A GUI for joinmarket"
    has_blueprint = True
    devstatus = devstatus_alpha
    blueprint_module = "jmf.controller"

    sort_priority=5
    
