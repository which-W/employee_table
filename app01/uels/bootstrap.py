from django import forms


class Father_modelform(forms.ModelForm):
    # Initialize the form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Loop through the fields in the form
        for name, filed in self.fields.items():
            # Check if the widget has attributes
            if filed.widget.attrs:
                # Set the class and placeholder attributes
                filed.widget.attrs["class"] = "form-control"
                filed.widget.attrs["placeholder"] = filed.label
            else:
                # Set the class and placeholder attributes
                filed.widget.attrs = {
                    "class": "form-control",
                    "placeholder": filed.label
                }
