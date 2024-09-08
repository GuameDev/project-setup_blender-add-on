
# Blender Project Setup Addon

## Overview

Blender Project Setup is an addon designed to streamline the process of creating structured project folders for Blender artists. The addon allows users to define a base path and project name, and automatically generates a well-organized folder structure to keep assets, models, textures, and other project elements properly categorized.

## Features

- Automatically create a structured folder system for new 3D projects.
- Customize base paths and project names.
- Default folder structure includes subfolders for:
  - Concepts (References, Sketches)
  - Models (Base Meshes, Sculpted Models, Retopology)
  - Textures (UV Maps, Baked Textures, Hand Painted)
  - Rigs (Bones, Controllers)
  - Animations (Walk Cycles, Facial Expressions)
  - Render (Preview, Final)
  - Backups (Old Versions, Auto Saves)
- Predefined folder templates you can select from, including Basic, Animation, Sculpting, and Game Development templates.
- Cross-platform support for Windows, macOS, and Linux with default base paths depending on the OS.

## Installation

1. Download the `.zip` file of the addon from the [releases page](https://github.com/GuameDev/Blender.Addon.ProjectSetup/releases/tag/v1.1.0).
2. Open Blender and navigate to `Edit` -> `Preferences`.
3. Go to the `Add-ons` tab and click on `Install...`.
4. Select the downloaded `.zip` file and click `Install Add-on from File`.
5. Enable the addon by checking the box next to **Blender Project Setup**.
6. You should now see a new panel under the `3D View` sidebar with project folder creation options.

## How to Use

1. Open Blender.
2. In the 3D View panel, find the new **Project Folders** tab.
3. Define your project name and base path or use the default base path.
4. Select a folder template from the dropdown (e.g., Basic, Animation, Sculpting, Game Development).
5. Click the `Create Project` button.
6. The addon will automatically create a structured folder setup for you based on the provided project name and base path.

### Folder Structure Example

```bash
MyNew3DProject/
│
├── 01_Concept
│   ├── References
│   └── Sketches
│
├── 02_Models
│   ├── Base_Meshes
│   ├── Sculpted_Models
│   └── Retopology
│
├── 03_Textures
│   ├── UV_Maps
│   ├── Baked_Textures
│   └── Hand_Painted
│
├── 04_Rigs
│   ├── Bones
│   └── Controllers
│
├── 05_Animations
│   ├── Walk_Cycles
│   └── Facial_Expressions
│
├── 06_Render
│   ├── Preview
│   └── Final
│
└── 07_Backups
    ├── Old_Versions
    └── Auto_Saves
```

## Available Templates

### Basic 3D Project

```bash
Folders:
01_References
02_Models
03_Textures
04_Rigs
05_Animations
06_Render
07_Backups
```

### Character Animation

```bash
Folders:
01_Concept_Art/References, Sketches
02_Models/Base_Mesh, High_Poly, Retopology, Final_Mesh
03_Textures/UV_Maps, Baked_Textures, Hand_Painted
04_Rigs/Skeleton, Controllers, Weight_Painting
05_Animations/Walk_Cycles, Facial_Animations
06_Render/Preview_Renders, Final_Renders
```

### Environmental Design Project

```bash
Folders:
01_References/Moodboards, Concept_Art
02_Scenes/Blocking, Final_Models
03_Textures/Ground_Materials, Tree_Bark, Water
04_Lighting/HDRIs, Sun_Sky
05_Renders/Preview, Final
```

### Game Asset Project

```bash
Folders:
01_Concept/References, Sketches
02_Models/Low_Poly, High_Poly, Retopology
03_Textures/UV_Maps, Baked_Textures, PBR_Materials
04_Exports/FBX, OBJ, GLTF
05_Final_Renders
```

## Development & Contribution

We welcome contributions to improve this addon. If you find any issues or have suggestions, please feel free to create an issue or submit a pull request.

### Running Unit Tests

The project includes unit tests for the domain logic. To run the tests:

1. Ensure you have Python installed.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the tests:

   ```bash
   python -m unittest discover -s tests
   ```

## License

This addon is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for more details.

---

**Author**: Pablo Muñoz
**Version**: 1.1.0  
**Blender Version**: 3.0 and above  
