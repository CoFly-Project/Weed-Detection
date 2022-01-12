<p align="center">
<img src="https://user-images.githubusercontent.com/77329407/105342573-3040e900-5be9-11eb-92df-7c09392b1e0c.png" width="300" />

# Weed-Detection
  
The main objective of the ```Weed-Detection``` module is to provide a more thorough inspection on problematic areas, as have been extracted from the [```Problematic-Areas-Detection```](https://github.com/CoFly-Project/Problematic-Areas-Detection) module in terms of plant health and provide valuable information to the end-user. In specific, the developed module is based on the pretrained DeepLabv3+ instance was pretrained on PASCAL VOC 2012 dataset and further trained on the  [```CoFly-WeedDB```](https://github.com/CoFly-Project/CoFly-WeedDB) dataset for the weed semantic segmentation task. The developed module is capable of semantically segmenting weed instances depicted on input RGB images and thus, provides accurate information regarding the location of detected weeds.
  
  
<p align="center">
<img src="https://user-images.githubusercontent.com/80779522/149145965-2b5b5da1-dfa5-4752-8794-e76d5f5ba16b.png"/>
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
    <td><img src= "https://user-images.githubusercontent.com/80779522/149173384-6b77ede1-7ba0-46ba-b2d7-b88faa354ed1.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149176316-31dea9dc-f404-450a-9571-737c9bf688f8.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149176331-4fbe5d4c-07f4-42b9-a7ef-69b31194abae.png" align="center" /></td> 
   </tr>
    <tr class="center">
    <td><img src= "https://user-images.githubusercontent.com/80779522/149164019-5fec6f1a-20dc-42af-9d27-cc8469c2c0ec.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149173382-e778d023-7a0f-4fe4-b8e6-b555c5560e46.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149176321-5af200eb-910e-4e21-bcc2-a2496fb63813.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149176398-62a1f5e9-42ea-40b7-b49e-f983dfd3b33e.png" align="center" /></td> 
   </tr> 
    <tr class="center">
    <td><img src= "https://user-images.githubusercontent.com/80779522/149163723-cc0b5cc6-d47f-426d-8c09-034d9191bb57.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149173373-3eee23c9-da9d-4290-887f-4d7645f35c41.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149176324-1d0218ad-a784-46e9-aaf6-4eb1ec656d48.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149176209-390166f1-ef29-49bc-ac6a-c15d86ce1671.png" align="center" /></td> 
   </tr>
    <tr class="center">
    <td><img src= "https://user-images.githubusercontent.com/80779522/149163873-6a608eb5-7cb1-425f-8e7b-2fec86e48cfe.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149173366-f44434ec-432c-4cf0-9c8b-8ead8a906671.png" align="center" /></td>
    <td><img src= "https://user-images.githubusercontent.com/80779522/149176329-8b5f8165-64a9-4172-abef-3630884d875d.png" align="center" /></td>  
    <td><img src= "https://user-images.githubusercontent.com/80779522/149176256-1d50e03d-8b67-4762-90d5-6059eb915c63.png" align="center" /></td> 
   </tr> 
 
   <tr align="center">
    <td>(a) Input RGB image</td>
    <td>(b) Ground truth</td>
    <td>(c) Predicted mask</td>   
    <td>(d) Overlay</td>
  </tr>  
 </table>
 
  <figcaption align = "center"><p align="center">
  Figure 2. Results from the Weed-Detection module with (a) RGB images as inputs (b) the ground truth and the corresponding (c) predicted masks and (d) overlays as extracted.
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
