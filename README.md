# Naval Architect - Marine Analysis [![Build Status](https://travis-ci.com/SevanSSP/Naval_Architect-Marine_Analysis.svg?branch=master)](https://travis-ci.com/SevanSSP/Naval_Architect-Marine_Analysis)
Before you apply for this position we first challenge you to a quiz on the topics hydrodynamics and coding.
The idea is to give you an opportunity to learn about some important topics for this position and demonstrate basic understanding.
We will require that all questions are aswered correctly to be considered, but we would like to see that an attempt is made on all questions.  

If you have stumbled upon this repository without reading the job ad first, please refer to 
[finn.no](http://www.finn.no/???) or [sevassp.com](http://www.sevanssp.com/???)

## Quiz
Hints and necessary code is found in the repository. All code is written in Python 3.6.

### Quiz sheet
Download the quiz sheet from this repository and add your answers to the questions below.  

### 1) 

### 2) Mooring chain properties
Chains are important components in the mooring system use to keep floating structures in place.

The task 2 Python file contains a simplified ```MooringChain``` class capable of returning the breaking strength and dry weight of chain in accordance with DNVGL-OS-E302 (or any other class society for that matter).
This class can be used to answer he following questions:

- What is the breaking strength of 157 mm R4S chain in kN?
- What is the dry mass per length of 84 mm stud chain in kg/m?

Be aware that the ```MooringChain``` class and its methods expect and return SI units.   

### 3)

### 4) Travis-CI
We apply [Travis CI](http://www.tracis-ci.com) for testing our code, building our packages and distributing them to [packager.com](http://app.packagr.com). 
The tests\ folder contains the tests for this repository. A proper set of tests should have checked all aspects of the codes found under e.g tasks\ . 
But that would make the quiz to easy. Instead we only test some recognised truths. The status of the testing is seen by the status icon at the top of this readme.

- What is the value of the ```HiddenValue``` environmental variable set in Travis for this repository?

### 5) Froude scaling
Model testing is a vital part of verifying the performance of a floating structure. 
Results in are converted from model to full scale under the assumption that the Froude number in both scales is identical (i.e. Froude scaling).

The complied python file for task 1 contains the following function:

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
506c6561736520777269746520612073686f7274206170706c69636174696f6e20616e642061747461636820796f757220435620616e6420746865207175697a2073686565742e20546865206170706c69636174696f6e2077697468206174746163686d656e7473207368616c6c2062652073656e7420746f206a6f6240736576616e7373702e636f6d2e
