# Naval Architect - Marine Analysis [![Build Status](https://travis-ci.com/SevanSSP/Naval_Architect-Marine_Analysis.svg?branch=master)](https://travis-ci.com/SevanSSP/Naval_Architect-Marine_Analysis)
Before you apply for this position, we first challenge you to a quiz on the topics hydrodynamics and coding.
The idea is to give you an opportunity to learn about some important topics for this position and demonstrate basic understanding.
We will not require that all questions are answered correctly to be considered, but we would like to see that an attempt is made on all questions.  

If you have stumbled upon this repository without reading the job ad first, please refer to 
[sevanssp.com](https://sevanssp.com/vacant-positions/) and [finn.no](https://www.finn.no/job/fulltime/ad.html?finnkode=165677959).

## Quiz
Hints and necessary code is found in the repository. All code is written in Python 3.6.

### Quiz sheet
Download the quiz sheet from the ```quiz\``` folder and add your answers to the questions below.  

### 1) Hex your name

- What is your name in hexadecimal form?

### 2) Mooring chain properties
Chains are important components in mooring systems used to keep floating structures in place.

The task 2 Python file contains a simplified ```MooringChain``` class capable of returning the breaking strength and dry weight of chain in accordance with DNVGL-OS-E302 (or any other class society, for that matter).
This class can be used to answer he following questions:

- What is the breaking strength of 157 mm R4S chain in kN?
- What is the dry mass per length of 84 mm stud chain in kg/m?

Be aware that the ```MooringChain``` class and its methods expect and return SI units.

### 3) Added mass and natural period
Global performance and natural period is important parameters for a floating structure.

The task 3 Python file contains a  ```Floater```, a ```Barge``` and a ```Cylinder``` classes that return added mass and natural period for a cylinder and a barge in accordance with approximated methods.
The classes can be used to answer the following questions:
 - What is the added mass of a cylinder with diameter = 100m? (Give the answer in tons)
 - What is the natural period of a barge with mass = 150,000t, length=300m, width=55m and draft=18m? 

Be aware that the ```Floater```, ```Barge``` and ```Cylinder``` classes and its methods expect and return SI units.

### 4) Travis-CI
We apply [Travis CI](http://www.travis-ci.com) for testing our code, building our packages and distributing them to [packagr.com](http://app.packagr.com).
The ```tests\``` folder contains the tests for this repository. A proper set of tests should have checked all aspects of the codes found under e.g ```quiz\```, but that would make the quiz too easy. 
Instead we only test some recognised truths. The status of the testing is seen by the status icon at the top of this readme.

- What is the value of the ```HiddenValue``` environmental variable set in Travis for this repository?

### 5) Froude scaling
Model testing is a vital part of verifying the performance of a floating structure. 
Results are converted from model to full scale under the assumption that the Froude number in both scales is identical (i.e. Froude scaling).

The complied Python file for task 5 contains the following function:

```python
def model_test_scaling(full_scale_diameter):
    """
    Scales and prints statistical parameters from 5 model test measurement 
    channels in the specified full scale. The model test scale is defined 
    by the waterline diameter of the full scale unit. 

    Parameters
    ----------
    full_scale_diameter: float
        Water line diameter (m) of full scale unit, which the model test 
        data is scaled to
    """    
```
The model test scaling produces incorrect results for one of the channels.

- Which channel scales incorrectly?
- Why is that channel incorrect? 


## Apply
48656164206261636b20746f20746865206a6f6220616420287777772e66696e6e2e6e6f2f6a6f622f66756c6c74696d652f61642e68746d6c3f66696e6e6b6f64653d3136353637373935392920616e64206170706c792074686572652e20506c65617365207375626d697420796f7572207175697a20736865657420616c6f6e67207769746820746865206170706c69636174696f6e20616e6420796f7572204356
