# **PACK-IT-UP**


### Objective : 
To provide Optimal Solution for food Packaging

### Problem Statement :
Bundling design for food items should be planned dependent on a simulation model. 
This model ought to give the ideal or optimum outcomes for the packing of the product (primarily cost).
A simulation needs to be done to get those optimum results.

### Solution :
A website in which the properties like chemical reactions and physical dimensions of the objects will be taken as an input from the user and then select the best suitable material for that in which product can sustain much longer also the most optimum orientation and design of the product which can minimize the area of packing.
In this whole process, the prime objective is cost optimization.


#### Stage 1:
 1. Design the front end of website.
 2. Implementation of backend frameworks.
 3. Create a demo data set.
 4. Prepare 'codebase.py' file and there should be the demo dataset of materials which are commonly used for packaging.


#### Stage 2:
A software service i.e website that will take the inputs of the certain properties like chemical reactions and physical dimensions of the product from the user, store it in our database and compare with the packaging material which is best suitable for that particular product.
This comparison will be done between the data which is pre-loaded in python file codebase.py and the user inputs. After a proper analysis of the properties of packing material which suits that product, a list of suitable materials will be generate.
The information in python file codebase.py is arbitary and random, real knowledge will be in the code to induce the precise results. obtaining the information from the base mistreatment pyrebase. 
<strong>Properties that will be taken as an input from the users are: </strong>
   * Physical Dimensions
   * State of the product
   * Chemical properties of product
      * Reaction with the oxygen
      * Photosensitive, etc.
   * Durability of product
   * Specified packaging material(ex. Tetrapack), etc.
   <br>
<strong>The factors on which packaging will be depend on :</strong>
   * All properties
      * Physical dimensions
      * Orientation of the product
      * Fragile nature
      * Durability / use before, etc.
    * Manufacturing state
      * Powder
      * Liquid
      * etc.
    * Packaging Materials
      * Plastic
      * Cardboard
      * Metal / Tin
      * Glass
    * Costing
      * Plastic
      * Cardboard
      * any other
    * etc.
    

For now, the scope of this project is limited to the solid objects (mainly biscuit) but can be extended to the other products as well.

#### Stage 3:

 1. Code in the "orientation.py" file.
 2. Create an algorithm that will test all the possible arrangements of the product in the packing and then return the one which is takes minimum surface area and is also sustainable.  
 3. Create the best arrangement of the product inside the packing, determine shape, size and surface area of the packing.
 4. Designing the front End for the results page.
 5. Using javascript for the processing page.

#### Stage 4:

 1. Code in the "packing.py" file.
 2. Then link the cost and properties of every material in "codebase.py" and then suggesting the best possible orientation with a logic in which we will find out the best optimum packaging for the product.
 3. Then link the codebase.py , orientation.py. From these files we'll find out the least area of all possible orientations and the best materials used for the product.
 5. connecting the firebase and the python file.
 6. Then importing the files "codebase.py" and "orientation.py" in "packing.py".
 7. Then process all the data in the form of list from "packing.py" to the firebase and then from to the websitea as well.
