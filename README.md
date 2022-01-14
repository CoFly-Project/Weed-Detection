<p align="center">
<img src="https://user-images.githubusercontent.com/77329407/105342573-3040e900-5be9-11eb-92df-7c09392b1e0c.png" width="300" />

# Weed-Detection
  
The main objective of the ```Weed-Detection``` module is to provide a more thorough inspection on problematic areas, as have been extracted from the [```Problematic-Areas-Detection```](https://github.com/CoFly-Project/Problematic-Areas-Detection) module in terms of plant health and provide valuable information to the end-user. In specific, the developed module is based on the pretrained DeepLabv3+ instance was pretrained on PASCAL VOC 2012 dataset and further trained on the  [```CoFly-WeedDB```](https://github.com/CoFly-Project/CoFly-WeedDB) dataset for the weed semantic segmentation task. The developed module is capable of semantically segmenting weed instances depicted on input RGB images and thus, provides accurate information regarding the location of detected weeds.
  
  
<p align="center">
<img src="https://user-images.githubusercontent.com/80779522/149207481-2a7fb4cb-309e-454b-8fab-103a518a2800.png"/>
<figcaption align = "center"><p align="center">
  Figure 1. Workflow of the Weed-Detection module. The detected weeds are annotated with pink color.
    </figcaption>
  
  
## How to run
  
1. Clone this repo
2. Open terminal on ~REPO_PATH
3. Run:
```
python3 weed_detection.py ~INPUT_FOLDER_PATH ~OUTPUT_FOLDER_PATH
```
**ARGUMEΝTS**
  * ```~INPUT_FOLDER_PATH```:  refers to the path of the folder where the images are stored
  * ```~OUTPUT_FOLDER_PATH```: refers to the path where extracted annotated images will be saved
  
## Results
  
### Visualizations   
  <table class="center">
   <tr class="center">
    <td><img src= "https://user-images.githubusercontent.com/80779522/148941318-6922edc4-a11e-47f7-8feb-71659367fe80.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149325086-f561b75f-51f2-4624-88fb-6649e9a740ac.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149202187-d4f62556-a42a-4bf3-a601-826848c9b23c.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149201959-c48a2f4f-c074-4b09-a286-2d6dbf4a9276.png" align="center" /></td> 
   </tr>
    <tr class="center">
    <td><img src= "https://user-images.githubusercontent.com/80779522/149515973-5fbf6dd8-5383-4a03-924b-b24a935de5fc.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149518612-27d5eac2-acec-49c3-a769-3412788b9a5a.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149515662-03f7a34a-0398-4ebf-b4a0-6a061cd6cc7a.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149515759-24be4d2e-a3b9-4d4f-9ba0-0256d069641e.png" align="center" /></td> 
   </tr> 
    <tr class="center">
    <td><img src= "https://user-images.githubusercontent.com/80779522/149202267-3c24a3dd-97d3-439b-b647-142bd64278a8.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149324545-a39c8edd-3c8b-4298-9c8b-b17278270c7a.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149202190-9fb88165-98e1-45e8-90f6-77e5c1ba55dd.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149202002-d49ab489-83a5-4ea7-98f0-90c9c7e7835b.png" align="center" /></td> 
   </tr>
    <tr class="center">
    <td><img src= "https://user-images.githubusercontent.com/80779522/149201857-eeb19a19-14e9-4dae-b3c6-0ed8886677a3.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149324548-6b5a1ef2-cfd7-488b-8292-fd372453f015.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149202195-9c0614c3-606d-402e-a84b-d389dbf35619.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149202098-b8eda456-4f4a-4ffa-ad88-8412dc38d47a.png" align="center" /></td> 
   </tr>
   <tr class="center">
    <td><img src= "https://user-images.githubusercontent.com/80779522/149201901-e90286db-6277-4220-b236-0587ff1ac385.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149324538-eb4238c9-f20e-45ab-a843-5295e13de105.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149202196-e54ae7a6-cc51-46f7-bc3e-7b38511b4dc3.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149202140-b268fc66-b533-4a92-a9d2-380baface177.png" align="center" /></td> 
   </tr> 
   <tr align="center">
    <td>(a) Input RGB image</td>
    <td>(b) Ground truth</td>
    <td>(c) Predicted mask</td>   
    <td>(d) Overlay</td>
  </tr>  
 </table>
 
  <figcaption align = "center"><p align="center">
  Figure 2. Results from the Weed-Detection module.
    </figcaption>

## Dependencies 
Install all the neccecary dependencies using ```pip3 install <package name>```

Required packages:
* opencv-python (version >= 4.5.3)
* numpy (version >= 1.19.5)
* matplotlib (version >= 3.2.2)
* tensorflow (version >= 2.7.0)
* keras (version == 2.7.0)
* segmentation-models (version == 1.0.1)

> Note: The versions of tensorflow, keras and segmentation-models should be compatible. 

## Citation
(not published yet)

## Acknowledgment
This research has been financed by the European Regional Development Fund of the European Union and Greek national funds through the Operational Program Competitiveness, Entrepreneurship and Innovation, under the call RESEARCH - CREATE - INNOVATE (T1EDK-00636).
