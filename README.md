# Project Setup - Blender Add-on

## Overview

**Blender Project Setup** is an addon designed to streamline the process of creating structured project folders for **Blender artists and game developers**. The addon allows users to define a base path and project name and automatically generates a well-organized folder structure for assets, models, textures, and other project elements.

## Features

- ✔ **Automatically create a structured folder system** for new 3D projects.  
- ✔ **Remembers the last selected base path** between Blender sessions.  
- ✔ **Predefined templates** for different workflows:  
  - **Basic 3D Project**
  - **Game Asset Development** (Unity/Substance Painter ready)  
  - **Character Animation**  
  - **Environment Design**  
- ✔ **Supports automatic `.blend` file creation** in key folders.  
- ✔ **OS-independent:** Works on **Windows, macOS, and Linux**.  

---

## 🚀 What's New in v1.2.0

### ✅ Persistent Last Selected Folder Path

- The addon **remembers the last selected base path** across Blender sessions.
- No need to reselect the project folder every time Blender restarts!

### ✅ Improved Folder Structure Templates

- Game Asset Project, Character Animation, and Environment Design templates now support:
  - **Ordered folders** (`01_Models`, `02_Textures`, etc.).
  - **Auto-generated `.blend` files** inside relevant folders.
  - **Initial `.blend` file flag** to define the project’s starting point.

### ✅ **Bug Fixes & Performance Enhancements**

- Fixed `.blend` file creation issues.
- Improved error handling and file storage efficiency.

---

## **📌 Installation**

1. **Download the latest `.zip` release** from [GitHub Releases](https://github.com/GuameDev/Blender.Addon.ProjectSetup/releases).
2. Open Blender and go to:
   - **Edit** → **Preferences** → **Add-ons**.
3. Click **Install...**, select the downloaded `.zip`, and enable the addon.

---

## 📌 How to Use

1. **Open Blender**.
2. Navigate to **3D View > Sidebar (`N` key) > Project Folders Panel**.
3. **Enter a project name** and select a **base path**.
4. **Choose a template** (e.g., Game Asset, Character Animation).
5. Click **"Create Project"**.
6. Blender will:
   - **Automatically create a structured folder setup**.
   - **Save the current `.blend` file** in the designated starting folder.
   - **Remember the last selected base path** for the next session.

---

## **📌 Folder Structure Example**

### Game Asset Project

```text
MyGameAsset/
│
├── 01_Concept_Art/
│   ├── References/
│   ├── Sketches/
│
├── 02_Models/
│   ├── ✅ Blockout/ (Initial `.blend` file)
│   ├── High_Poly/
│   ├── Low_Poly/
│   ├── Retopology/
│   ├── UV/
│
├── 03_Baking/
│   ├── Baked_Textures/
│   ├── ID_Maps/
│   ├── AO_Maps/
│
├── 04_Textures/
│   ├── UV_Maps/
│   ├── **Material_Projects/** (Stores `.spp`, `.blend`, etc.)
│   ├── PBR_Materials/
│
├── 05_Exports/
│   ├── FBX/
│   ├── OBJ/
│   ├── GLTF/
│   ├── Unity_Prefabs/
│
└── 06_Final_Renders/
    ├── 🆕 SciFiWeapon-Final_Renders.v0.1.blend
```

---

## **📌 Development & Contribution**

We welcome contributions! If you find any issues or have suggestions, please:

- **Create an issue** on GitHub.
- **Submit a pull request** for improvements.

---

## **📌 License**

This addon is licensed under the **GNU General Public License v3.0**.  
See the [LICENSE](LICENSE) file for more details.

---

**Author**: Your Name  
**Version**: **v1.2.0**  
**Blender Version**: **3.0 and above**  
