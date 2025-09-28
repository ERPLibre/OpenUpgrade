# Copyright 2025 TechnoLibre  <https://technolibre.ca>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import logging

from openupgradelib import openupgrade

from odoo.tools.translate import _

_logger = logging.getLogger(__name__)


def change_owner_group_fiscal_year(env):
    """When installing om_account_accountant, got a conflict duplicated group group_fiscal_year"""
    imd = env["ir.model.data"].sudo()
    # Remove any stale/duplicate mapping of the old XMLID
    imd.search(
        [
            ("module", "=", "account"),
            ("name", "=", "group_fiscal_year"),
            ("model", "=", "res.groups"),
        ]
    ).unlink()
    imd = env["res.groups"].sudo()
    # Remove any stale/duplicate mapping of the old XMLID
    imd.search(
        [
            (
                "name",
                "=",
                "Allow to define fiscal years of more or less than a year",
            ),
        ]
    ).unlink()


@openupgrade.migrate()
def migrate(env, version):
    change_owner_group_fiscal_year(env)
