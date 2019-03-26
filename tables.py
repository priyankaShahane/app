from flask_table import Table, Col, LinkCol


class Results(Table):
    productID = Col('productID')
    productName = Col('productName')
    Quantity = Col('Quantity')
    cost = Col('cost')
    edit = LinkCol('Edit', 'edit_view', url_kwargs=dict(id='productID'))



class Result(Table):
    locationID = Col('locationID')
    locationName = Col('locationName')
    store = Col('store')
    productID = Col('productID')
    edit = LinkCol('Edit', 'edit_location_view', url_kwargs=dict(id='locationID'))



class Result1(Table):
    movementID = Col('movementID')
    fromLocation = Col('fromLocation')
    toLocation = Col('toLocation')
    productID = Col('productID')
    Quantity = Col('Quantity')
    created = Col('created')
    edit = LinkCol('Edit', 'edit_product_movement_view', url_kwargs=dict(id='movementID'))