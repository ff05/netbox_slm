from django import forms
from extras.forms import (
    CustomFieldModelForm,
    CustomFieldModelCSVForm,
    AddRemoveTagsForm,
    CustomFieldModelBulkEditForm,
    CustomFieldModelFilterForm,
)
from dcim.models import Manufacturer
from netbox_slm.models import SoftwareProduct, SoftwareProductVersion
from utilities.forms import (
    BootstrapMixin, DynamicModelChoiceField,
)


from netbox_slm.fields import CustomDynamicModelMultipleChoiceField


class SoftwareProductForm(BootstrapMixin, CustomFieldModelForm):
    """Form for creating a new SoftwareProduct object."""

    manufacturer = DynamicModelChoiceField(
        queryset=Manufacturer.objects.all(),
        required=False,
        # initial_params={
        #     'device_types': 'device_type'
        # }
    )

    # tags = DynamicModelMultipleChoiceField(
    #     queryset=Tag.objects.all(),
    #     required=False,
    # )

    class Meta:
        model = SoftwareProduct
        fields = ("name", "manufacturer",)  # "tags")


class SoftwareProductFilterForm(BootstrapMixin, CustomFieldModelFilterForm):
    """Form for filtering SoftwareProduct instances."""

    model = SoftwareProduct

    q = forms.CharField(required=False, label="Search")

    name = forms.CharField(
        required=False,
        label="Name",
    )

    # tag = TagFilterField(SoftwareProduct)


class SoftwareProductCSVForm(CustomFieldModelCSVForm):
    class Meta:
        model = SoftwareProduct
        fields = ("name",)


class SoftwareProductBulkEditForm(BootstrapMixin, AddRemoveTagsForm, CustomFieldModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=SoftwareProduct.objects.all(),
        widget=forms.MultipleHiddenInput(),
    )

    class Meta:
        nullable_fields = []


class SoftwareProductVersionForm(BootstrapMixin, CustomFieldModelForm):
    """Form for creating a new SoftwareProductVersion object."""

    software_product = CustomDynamicModelMultipleChoiceField(
        queryset=SoftwareProduct.objects.all(),
        required=False,
        # initial_params={
        #     'device_types': 'device_type'
        # }
    )

    # tags = DynamicModelMultipleChoiceField(
    #     queryset=Tag.objects.all(),
    #     required=False,
    # )

    class Meta:
        model = SoftwareProductVersion
        fields = ("name", "software_product",)  # "tags")


class SoftwareProductVersionFilterForm(BootstrapMixin, CustomFieldModelFilterForm):
    """Form for filtering SoftwareProductVersion instances."""

    model = SoftwareProductVersion

    q = forms.CharField(required=False, label="Search")

    name = forms.CharField(
        required=False,
        label="Name",
    )

    # tag = TagFilterField(SoftwareProduct)


class SoftwareProductVersionCSVForm(CustomFieldModelCSVForm):
    class Meta:
        model = SoftwareProductVersion
        fields = ("name",)


class SoftwareProductVersionBulkEditForm(BootstrapMixin, AddRemoveTagsForm, CustomFieldModelBulkEditForm):
    pk = forms.ModelMultipleChoiceField(
        queryset=SoftwareProduct.objects.all(),
        widget=forms.MultipleHiddenInput(),
    )

    class Meta:
        nullable_fields = []
