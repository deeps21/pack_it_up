# **PACK-IT-UP**
## **Optimal Solution for food Packaging**


### Problem Statement :
Packaging format for food products need to be designed based on a simulation model.
This model should provide the optimum results for the packing of the product mostly cost.
A simulation has to be done basis forces that products undergo during the journey in the supply chain.

### Solution :
A website in which the properties of the objects will be taken as an input and then select the best suitable material for that in which
object can sustain much longer also the most optimum orientation and design of the product which can minimize the area of packing.
In this whole process the cost optimization is the prime objective.


#### Stage 1:
- [x] 1. Make front end of website.
- [x] 2. Implementation of backend frameworks.
- [x] 3. Ccreate a demo data set.
- [x] 4. Prepare 'codebase.py' file. In this file there should be the demo dataset of some materials which are commonly used for packaging.


#### Stage 2:
- [x] A website that will take the inputs of the certain properties of the object from the user, store it in database and compare with the package material which is best suitable for that object.
This comparison is done between the data which is pre-loaded in file `codebase.py` and the user inputs. After a careful analysis of the properties of packing material which suits the object, a list is generated of suitable materials.
All the data in `codebase.py` is arbitary and random, real data can be used in the code to get the exact results.
Getting the data from the firebase using `pyrebase`.
<strong>Properties which are taken as an input from the users are: </strong>
   * Dimensions
   * State of product
   * Chemical properties
      * Reaction with oxygen
      * Photosensitive, etc.
   * Durability of product
   * Packaging material specified(ex. Tetrapack), etc.
   <br>
<strong>Constraints and factors on which packaging depends on:</strong>
For Solid:

    * All properties
      * Dimensions
      * Orientation of product
      * Fragile nature
      * Durability / use before, etc.
    * Manufacturing state
      * Powder
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

The scope of this project is limited to the solid objects (mainly biscuit) but can be extended to the other objects as well.
