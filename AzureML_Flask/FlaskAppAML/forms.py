from wtforms import Form, StringField, TextAreaField, validators


class SubmissionForm(Form):
    RegionID = StringField('RegionID')
    Stock_Market = StringField('Stock_Market')
    Mortgage_Rate = StringField('Mortgage_Rate')
    Monthly_Supply_Of_Homes = StringField('Monthly_Supply_Of_Homes')