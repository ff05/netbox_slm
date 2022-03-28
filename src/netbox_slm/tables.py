import django_tables2 as tables
from django_tables2.utils import Accessor
from netbox_slm.models import SoftwareProduct, SoftwareProductVersion, SoftwareProductInstallation
from utilities.tables import BaseTable, ChoiceFieldColumn, ToggleColumn


class SoftwareProductTable(BaseTable):
    """Table for displaying SoftwareProduct objects."""

    pk = ToggleColumn()
    name = tables.LinkColumn()
    manufacturer = tables.Column(
        accessor=Accessor('manufacturer'),
        linkify=True
    )
    installations = tables.Column(accessor='get_installation_count', verbose_name='Installations')

    # tags = TagColumn(
    #     url_name="plugins:netbox_dns:zone_list",
    # )

    class Meta(BaseTable.Meta):
        model = SoftwareProduct
        fields = (
            "pk",
            "name",
            "manufacturer",
            "description",
            "installations",
            # "tags",
        )
        default_columns = (
            "pk",
            "name",
            "manufacturer",
            "description",
            "installations",
            # "tags",
        )
        sequence = (
            "manufacturer",
            "name",
            "description",
            "installations",
        )


class SoftwareProductVersionTable(BaseTable):
    """Table for displaying SoftwareProductVersion objects."""

    pk = ToggleColumn()
    name = tables.LinkColumn(verbose_name='Version')
    software_product = tables.Column(
        accessor=Accessor('software_product'),
        linkify=True
    )
    manufacturer = tables.Column(
        accessor=Accessor('software_product__manufacturer'),
        linkify=True
    )
    installations = tables.Column(accessor='get_installation_count', verbose_name='Installations')

    # tags = TagColumn(
    #     url_name="plugins:netbox_dns:zone_list",
    # )

    class Meta(BaseTable.Meta):
        model = SoftwareProductVersion
        fields = (
            "pk",
            "name",
            "software_product",
            "manufacturer",
            "installations",
            # "tags",
        )
        default_columns = (
            "pk",
            "name",
            "software_product",
            "manufacturer",
            "installations",
            # "tags",
        )
        sequence = (
            "manufacturer",
            "software_product",
            "name",
            "installations",
        )


class SoftwareProductInstallationTable(BaseTable):
    """Table for displaying SoftwareProductInstallation objects."""

    pk = ToggleColumn()
    name = tables.LinkColumn()
    device = tables.Column(
        accessor=Accessor('device'),
        linkify=True
    )
    virtualmachine = tables.Column(
        accessor=Accessor('virtualmachine'),
        linkify=True
    )
    platform = tables.Column(
        accessor='get_platform',
        linkify=True
    )
    type = tables.Column(accessor='render_type')
    software_product = tables.Column(
        accessor=Accessor('software_product'),
        linkify=True
    )
    version = tables.Column(
        accessor=Accessor('version'),
        linkify=True
    )

    # tags = TagColumn(
    #     url_name="plugins:netbox_dns:zone_list",
    # )

    class Meta(BaseTable.Meta):
        model = SoftwareProductInstallation
        fields = (
            "pk",
            "name",
            "platform",
            "type",
            "software_product",
            "version",
            # "tags",
        )
        default_columns = (
            "pk",
            "platform",
            "type",
            "software_product",
            "version",
            # "tags",
        )

    def render_software_product(self, value, **kwargs):
        return f"{kwargs['record'].software_product.manufacturer.name} - {value}"
