from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    l10n_do_dgii_start_date = fields.Date("Activities Start Date")
    l10n_do_ecf_issuer = fields.Boolean(
        "Is e-CF issuer",
        help="When activating this field, NCF issuance is disabled.",
    )
    l10n_do_ecf_deferred_submissions = fields.Boolean(
        "Deferred submissions",
        help="Identify taxpayers who have been previously authorized "
        "to have sales through offline mobile devices such as "
        "sales with Handheld, enter others.",
    )
    l10n_do_disable_fiscal_documents = fields.Boolean(
        string="Disable Fiscal Documents",
        help="Disable Dominican fiscal document management for this company.",
    )

    def _localization_use_documents(self):
        """Dominican localization uses documents"""
        self.ensure_one()
        if self.l10n_do_disable_fiscal_documents:
            return False
        return (
            True
            if self.country_id == self.env.ref("base.do")
            else super()._localization_use_documents()
        )
