from flask import Flask
from flask import Flask, redirect, render_template, request, session, url_for, logging, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os
from passlib.hash import sha256_crypt
from datetime import timedelta
from tables import Results
from tables import Result
from tables import Result1

from datetime import datetime
engine = create_engine("mysql+pymysql://root:root123456@localhost/inventory_management")
# (mysql+pymysql://username:password@localhost/databasename)
db = scoped_session(sessionmaker(bind=engine))

app = Flask(__name__)
app.secret_key = os.urandom(24)
app.permanent_session_lifetime=timedelta(minutes=8)


@app.route('/new_product')
def add_product_view():
    return render_template('add.html')

@app.route('/new_location')
def add_location_view():
    return render_template('add_location.html')

@app.route('/new_product_movement')
def add_product_movement_view():
    return render_template('add_product_movement.html')

@app.route('/add_product_movement', methods=["GET", "POST"])
def add_product_movement():
    if request.method == "POST":
        movementID = request.form.get("movementID")
        fromLocation = request.form.get("fromLocation")
        toLocation = request.form.get("toLocation")
        productID = request.form.get("productID")
        Quantity = request.form.get("Quantity")

        if movementID and productID and Quantity and fromLocation and toLocation:
            Quantitydata1 = db.execute("SELECT Quantity FROM product_movement WHERE (productID=:productID) AND (fromLocation=:fromLocation OR toLocation=:toLocation)",
                                          {"productID": productID,"fromLocation":fromLocation,"toLocation":fromLocation}).fetchone()
            if Quantitydata1 :
                quant = int(Quantitydata1[0])
                Quantitydata2 = db.execute(
                        "SELECT Quantity FROM product_movement WHERE (productID=:productID) AND (fromLocation=:fromLocation OR toLocation=:toLocation)",
                        {"productID": productID, "fromLocation": toLocation, "toLocation": toLocation}).fetchone()
                Quantity = int(Quantity)
                movementID1 = int(movementID) + 1
                Subtract = quant - Quantity
                if Subtract > Quantity or Subtract == Quantity or Subtract < Quantity:
                    db.execute(
                                "INSERT INTO product_movement(movementID,fromLocation,productID,Quantity)VALUES(:movementID,:fromLocation,:productID,:Quantity)",
                                {"movementID": movementID, "fromLocation": fromLocation, "productID": productID,
                                 "Quantity": Subtract})
                    db.commit()
                    if Quantitydata2:
                        Quantity = int(Quantity)
                        quantity1=int(Quantitydata2[0])
                        Quantity=int(Quantity) + int(quantity1)
                    else:
                        Quantity = int(Quantity)
                    db.execute(
                                "INSERT INTO product_movement(movementID,toLocation,productID,Quantity)VALUES(:movementID,:toLocation,:productID,:Quantity)",
                                {"movementID": movementID1, "toLocation": toLocation, "productID": productID,
                                 "Quantity": Quantity})
                    db.commit()
                    r = db.execute("select MAX(locationID) from location_table").fetchone()
                    db.commit()
                    locationID1 = r[0]
                    locationID = int(locationID1) + 1
                    db.execute(
                                "INSERT INTO location_table(locationID,locationName,store,productID)VALUES(:locationID,:locationName,:store,:productID)",
                                {"locationID": locationID, "locationName": toLocation, "store": " ",
                                 "productID": productID})
                    db.commit()

                    flash("product moved successfully...", "success")
                elif quant == Quantity:
                    db.execute(
                                "INSERT INTO product_movement(movementID,fromLocation,productID,Quantity)VALUES(:movementID,:fromLocation,:productID,:Quantity)",
                                {"movementID": movementID, "fromLocation": fromLocation, "productID": productID,
                                 "Quantity": Subtract})
                    db.commit()
                    db.execute(
                                "INSERT INTO product_movement(movementID,toLocation,productID,Quantity)VALUES(:movementID,:toLocation,:productID,:Quantity)",
                                {"movementID": movementID1, "toLocation": toLocation, "productID": productID,
                                 "Quantity": Quantity})
                    db.commit()
                    r = db.execute("select MAX(locationID) from location_table").fetchone()
                    db.commit()
                    locationID1 = r[0]
                    locationID = int(locationID1) + 1
                    db.execute(
                                "INSERT INTO location_table(locationID,locationName,store,productID)VALUES(:locationID,:locationName,:store,:productID)",
                                {"locationID": locationID, "locationName": toLocation, "store": " ",
                                 "productID": productID})
                    db.commit()
                    flash("product moved successfully...", "success")
                elif (Subtract < 0):
                    flash("insufficient products !! can not move...", "danger")

                return redirect(url_for('product_movement'))
            elif Quantitydata1 is None:
                Quantitydata = db.execute("SELECT Quantity FROM product_table WHERE productID=:productID",
                                      {"productID": productID}).fetchone()
                quant=int(Quantitydata[0])
                Quantity=int(Quantity)
                movementID1=int(movementID)+1
                if quant is None:
                    flash("enter valid productID","danger")
                else:
                    Subtract = quant - Quantity
                    if Subtract > Quantity or Subtract == Quantity or Subtract < Quantity:
                        db.execute("INSERT INTO product_movement(movementID,fromLocation,productID,Quantity)VALUES(:movementID,:fromLocation,:productID,:Quantity)",
                            {"movementID": movementID, "fromLocation": fromLocation, "productID": productID,"Quantity":Subtract})
                        db.commit()
                        db.execute("INSERT INTO product_movement(movementID,toLocation,productID,Quantity)VALUES(:movementID,:toLocation,:productID,:Quantity)",
                            {"movementID": movementID1, "toLocation": toLocation, "productID": productID,
                            "Quantity": Quantity})
                        db.commit()
                        r = db.execute("select MAX(locationID) from location_table").fetchone()
                        db.commit()
                        locationID1 = r[0]
                        locationID = int(locationID1) + 1
                        db.execute(
                            "INSERT INTO location_table(locationID,locationName,store,productID)VALUES(:locationID,:locationName,:store,:productID)",
                            {"locationID": locationID, "locationName": toLocation, "store": " ", "productID": productID})
                        db.commit()
                        flash("product moved successfully...", "success")
                    elif quant == Quantity:
                        db.execute(
                            "INSERT INTO product_movement(movementID,fromLocation,productID,Quantity)VALUES(:movementID,:fromLocation,:productID,:Quantity)",
                            {"movementID": movementID, "fromLocation": fromLocation, "productID": productID,
                            "Quantity": Subtract})
                        db.commit()
                        db.execute(
                            "INSERT INTO product_movement(movementID,toLocation,productID,Quantity)VALUES(:movementID,:toLocation,:productID,:Quantity)",
                            {"movementID": movementID1, "toLocation": toLocation, "productID": productID,
                            "Quantity": Quantity})
                        db.commit()
                        r = db.execute("select MAX(locationID) from location_table").fetchone()
                        db.commit()
                        locationID1 = r[0]
                        locationID = int(locationID1) + 1
                        db.execute(
                            "INSERT INTO location_table(locationID,locationName,store,productID)VALUES(:locationID,:locationName,:store,:productID)",
                            {"locationID": locationID, "locationName": toLocation, "store": " ", "productID": productID})
                        db.commit()
                        flash("product moved successfully...", "success")
                        return redirect(url_for('product_movement'))
                    elif(Subtract < 0):
                        flash("insufficient products !! can not move...", "danger")
                        return redirect(url_for('product_movement'))
            else:
                flash("Error while adding location", "danger")
    return redirect(url_for('product_movement'))

@app.route('/add_location', methods=["GET", "POST"])
def add_location():
    if request.method == "POST":
        locationID = request.form.get("locationID")
        locationName = request.form.get("locationName")
        Store = request.form.get("Store")
        productID = request.form.get("productID")

        if locationID and locationName and Store :
            productIDdata = db.execute("SELECT * FROM product_table WHERE productID=:productID",
                                      {"productID": productID}).fetchone()
            if productIDdata is None:
                flash("enter valid productID","danger")
            else:
                db.execute("INSERT INTO location_table(locationID,locationName,store,productID)VALUES(:locationID,:locationName,:Store,:productID)",
                       {"locationID": locationID, "locationName": locationName, "Store": Store,"productID":productID})
                db.commit()
                flash("location added successfully...", "success")
                return redirect(url_for('location'))
        else:
            flash("Error while adding location", "danger")

@app.route('/product_balance', methods=["GET", "POST"])
def product_balance():
    row = db.execute("SELECT  a.productName,b.locationName,c.Quantity from product_table a inner join location_table b on a.productID=b.productID inner join product_movement c on  (b.productID=c.productID and b.locationName=c.fromLocation) or (b.productID=c.productID and b.locationName=c.toLocation)").fetchall()
    if row:
        return render_template('product_balance.html' ,row=row)
    else:
        flash("Error", "danger")
    return render_template('product_balance.html')
@app.route('/add', methods=["GET", "POST"])
def add_product():
    if request.method == "POST":
        productID = request.form.get("productID")
        productName = request.form.get("productName")
        quantity = request.form.get("quantity")
        cost = request.form.get("cost")

        if productID and productName and quantity and cost and request.method == 'POST':
            db.execute("INSERT INTO product_table(productID,productName,Quantity,cost)VALUES(:productID,:productName,:quantity,:cost)",
                       {"productID": productID, "productName": productName, "quantity": quantity,"cost":cost})
            db.commit()
            flash("product added successfully...", "success")
            return redirect(url_for('product'))
        else:
            flash("Error while adding product", "danger")




@app.route('/')
def home():
    return render_template('home.html')


# register form
@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form.get("name")
        username = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirm")
        secure_password = sha256_crypt.encrypt(str(password))

        if password == confirm:
            db.execute("INSERT INTO users(name,username,password)VALUES(:name,:username,:password)",
                       {"name": name, "username": username, "password": secure_password})
            db.commit()
            flash("You are registered successfully and can login...", "success")
            return redirect(url_for('login'))
        else:
            flash("password does not match", "danger")
            return render_template("register.html")

    return render_template('register.html')


# login form
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("name")
        password = request.form.get("password")

        usernamedata = db.execute("SELECT username FROM users WHERE username=:username",
                                  {"username": username}).fetchone()
        passwordata = db.execute("SELECT password FROM users WHERE username=:username",
                                 {"username": username}).fetchone()

        if usernamedata is None:
            flash("no username", "danger")
            return render_template("login.html")
        else:
            for password_data in passwordata:
                if sha256_crypt.verify(password, password_data):
                    session["log"] = True

                    flash("You are now login", "success")
                    return redirect(url_for('product'))

                else:
                    flash("incorrect password ", "danger")
                    return render_template("login.html")

    return render_template('login.html')


# product
@app.route('/product', methods=["GET", "POST"])
def product():
    productdata = db.execute("SELECT * FROM product_table").fetchall()
    db.commit()
    table = Results(productdata)
    table.border = True
    return render_template('product.html', table=table)

@app.route('/edit/<int:id>')
def edit_view(id):
    row=db.execute("SELECT * FROM product_table WHERE productID=:id",{"id": id}).fetchone()
    if row:
        return render_template('edit.html', row=row)
    else:
        flash("Error","danger")

@app.route('/edit_location/<int:id>')
def edit_location_view(id):
    row=db.execute("SELECT * FROM location_table WHERE locationID=:id",{"id": id}).fetchone()
    if row:
        return render_template('edit_location.html', row=row)
    else:
        flash("Error","danger")


@app.route('/edit_product_movement/<int:id>')
def edit_product_movement_view(id):
    #r=db.execute("select * From product_movement WHERE movementID=:id",{"id": id}).fetchall()
    #flash(r[0])
    #for records in r:
    row1 = db.execute(
        "SELECT * FROM product_movement e1, product_movement e2 WHERE e1.created= e2.created and e1.movementID != e2.movementID and e1.movementID=:id",
        {"id": id}).fetchall()
    # flash(row1[0])
    row = []
    if row1:
        for records in row1:
            row.append(records[0])
            if records[1] is None:
                row.append(records[7])
            else:
                row.append(records[1])
            if records[2] is None:
                row.append(records[8])
            else:
                row.append(records[2])
            row.append(records[3])
            if records[1] is None:
                row.append(records[4])
            else:
                row.append(records[10])
        return render_template('edit_product_movement.html', row=row)
    else:
        r = db.execute("select * From product_movement WHERE movementID=:id", {"id": id}).fetchall()
        for records in r:
            row.append(records[0])
            row.append(records[1])
            row.append(records[2])
            row.append(records[3])
            row.append(records[4])
        return render_template('edit_product_movement.html', row=row)

@app.route('/update', methods=["GET", "POST"])
def update_product():
    if request.method == "POST":
        productID = request.form.get("id")
        productName = request.form.get("productName")
        Quantity = request.form.get("Quantity")
        cost = request.form.get("cost")

        if productID and productName and Quantity and cost:
            db.execute("UPDATE product_table SET  productName=:productName, Quantity=:Quantity ,cost=:cost WHERE productID=:productID",{"productName": productName, "Quantity": Quantity, "cost": cost,"productID":productID})
            db.commit()
            flash("Product updated successfully!","success")
            return redirect('/product')
        else:
            flash("error","danger")
            return redirect('/product')

@app.route('/update_product_movement', methods=["GET", "POST"])
def update_product_movement():
    if request.method == "POST":
        movementID = request.form.get("movementID")
        fromLocation = request.form.get("fromLocation")
        toLocation = request.form.get("toLocation")
        productID = request.form.get("productID")
        Quantity = request.form.get("Quantity")

        if movementID and productID and Quantity and fromLocation and toLocation:
            Quantitydata = db.execute("SELECT Quantity FROM product_table WHERE productID=:productID",
                                          {"productID": productID}).fetchone()
            quant = int(Quantitydata[0])
            Quantity = int(Quantity)

            row1 = db.execute(
                "SELECT * FROM product_movement e1, product_movement e2 WHERE e1.created= e2.created and e1.movementID != e2.movementID and e1.movementID=:id",
                {"id": movementID}).fetchall()
            for r in row1:
                if r[1]:
                    movementID1 = int(movementID) + 1
                else:
                    movementID1=movementID
                    movementID = int(movementID) - 1

            if quant is None:
                flash("enter valid productID", "danger")
            else:
                Subtract = quant - Quantity
                if Subtract > Quantity or Subtract == Quantity or Subtract < Quantity:
                    db.execute("UPDATE product_movement SET  fromLocation=:fromLocation ,productID=:productID , Quantity=:Quantity WHERE movementID=:movementID",{"fromLocation": fromLocation,"productID":productID, "Quantity": Subtract,"movementID":movementID})
                    db.commit()
                    db.execute("UPDATE product_movement SET  toLocation=:toLocation ,productID=:productID,Quantity=:Quantity WHERE movementID=:movementID",{"toLocation": toLocation, "productID":productID,"Quantity": Quantity,"movementID":movementID1})
                    db.commit()
                    r = db.execute("select MAX(locationID) from location_table").fetchone()
                    db.commit()
                    #for r1 in r:
                    locationID1 = r[0]
                    locationID=int(locationID1)+1
                    flash(locationID)
                    db.execute(
                        "INSERT INTO location_table(locationID,locationName,store,productID)VALUES(:locationID,:locationName,:store,:productID)",
                        {"locationID": locationID, "locationName": toLocation,"store":" ","productID": productID})
                    db.commit()
                    flash("Product_movement updated successfully!","success")
                    return redirect('/product_movement')
                elif quant == Quantity:
                    db.execute(
                        "UPDATE product_movement SET  fromLocation=:fromLocation ,productID=:productID , Quantity=:Quantity WHERE movementID=:movementID",
                        {"fromLocation": fromLocation, "productID": productID, "Quantity": Subtract,
                         "movementID": movementID})
                    db.commit()
                    db.execute(
                            "UPDATE product_movement SET toLocation=:toLocation,productID=:productID,Quantity=:Quantity WHERE movementID=:movementID",{"toLocation":toLocation,"productID":productID,"Quantity":Quantity,"movementID":movementID1})
                    db.commit()
                    r = db.execute("select MAX(locationID) from location_table").fetchone()
                    db.commit()
                    # for r1 in r:
                    locationID1 = r[0]
                    locationID = int(locationID1) + 1
                    flash(locationID)
                    db.execute(
                        "INSERT INTO location_table(locationID,locationName,store,productID)VALUES(:locationID,:locationName,:store,:productID)",
                        {"locationID": locationID, "locationName": toLocation, "store": " ", "productID": productID})
                    db.commit()
                    flash("product movement updated successfully...", "success")
                    return redirect('/product_movement')
                elif(Subtract < 0):
                    flash("insufficient products !! can not move...", "danger")



    return redirect(url_for('product_movement'))


@app.route('/update_location', methods=["GET", "POST"])
def update_location():
    if request.method == "POST":
        locationID = request.form.get("id")
        locationName = request.form.get("locationName")
        store = request.form.get("store")
        productID = request.form.get("productID")

        if productID and locationID and locationName :
            sql = db.execute("UPDATE location_table SET  locationName=:locationName, store=:store , productID=:productID WHERE locationID=:locationID",{"locationName": locationName, "store": store, "productID": productID,"locationID":locationID})
            db.commit()
            flash("User updated successfully!","success")
            return redirect('/location')
        else:
            flash("error","danger")
            return redirect('/location')

@app.route('/delete_location/<int:id>')
def delete_location(id):

		db.execute("DELETE FROM location_table WHERE locationID=:id", {"id":id})
		db.commit()
		flash('location deleted successfully!')
		return redirect('/location')

@app.route('/delete/<int:id>')
def delete_product(id):

		db.execute("DELETE FROM product_table WHERE productID=:id", {"id":id})
		db.commit()
		flash('location deleted successfully!')
		return redirect('/product')

# location
@app.route('/location')
def location():
    locationdata = db.execute("SELECT * FROM location_table").fetchall()
    db.commit()
    table = Result(locationdata)
    table.border = True
    return render_template('location.html', table=table)



# Product_movement
@app.route('/product_movement')
def product_movement():
    product_movementdata = db.execute("SELECT * FROM product_movement").fetchall()
    db.commit()
    table = Result1(product_movementdata)
    table.border = True
    return render_template('product_movement.html', table=table)

# logout
@app.route('/logout')
def logout():
    session.clear()
    flash("You are now log out", "success")
    return render_template('home.html')


if __name__ == "__main__":
    app.run(debug=True)
