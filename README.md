<p align="center">
<img src="https://user-images.githubusercontent.com/77329407/105342573-3040e900-5be9-11eb-92df-7c09392b1e0c.png" width="300" />

# Weed-Detection
  
The main objective of the ```Weed-Detection``` module is to provide a more thorough inspection on problematic areas, as have been extracted from the [```Problematic-Areas-Detection```](https://github.com/CoFly-Project/Problematic-Areas-Detection) module in terms of plant health and provide valuable information to the end-user. In specific, the developed module is based on the pretrained DeepLabv3+ instance was pretrained on PASCAL VOC 2012 dataset and further trained on the  [```CoFly-WeedDB```](https://github.com/CoFly-Project/CoFly-WeedDB) dataset for the weed semantic segmentation task. The developed module is capable of semantically segmenting weed instances depicted on input RGB images and thus, provides accurate information regarding the location of detected weeds.
  
  
<p align="center">
<img src=""/>
<figcaption align = "center"><p align="center">
  Figure 2. Detected weeds annotated with pink color.
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
    
  
Examples of the CoFly-WeedDB dataset.
<table class="center">
  <tr class="center">
    <td><img src="https://user-images.githubusercontent.com/80779522/148941318-6922edc4-a11e-47f7-8feb-71659367fe80.png" =500x500 /></td>
    <td><img src="https://user-images.githubusercontent.com/80779522/148940518-fe3bd215-745f-45cf-883e-c7d1bb921cf6.png" =500x500 /></td>
    </tr>
  <tr class="center">
    <td><img src="https://user-images.githubusercontent.com/80779522/148941430-b8d319fc-66ea-43ee-97be-d1c2bd6b6685.png" =500x500/></td>  
    <td><img src="https://user-images.githubusercontent.com/80779522/148940616-39bb486e-5b42-4ba6-8c24-e8d383b0ec26.png" =500x500 /></td>
     </tr>
  <tr align="center">
    <td>(a) RGB</td>
    <td>(b) Overlay</td>
  </tr>
</table>
     <figcaption align = "center"><p align="center">
  Figure 2. Detected weeds annotated with pink color.
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

