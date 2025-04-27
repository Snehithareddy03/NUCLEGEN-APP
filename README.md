# rna
RNA Secondary Structure App is a cross-platform mobile application developed using Flutter in Android Studio. It allows users to input RNA sequences and predict their secondary structures using established thermodynamic algorithms. The app is designed to provide an accessible, mobile-friendly solution for bioinformatics students, researchers, and educators who need fast and interactive RNA folding analysis.

Users can enter RNA sequences manually or upload them from local storage. Once the sequence is submitted, it is sent to a backend server, where tools such as ViennaRNA or RNAfold process the data and return the predicted secondary structure in dot-bracket notation. The app then parses and visualizes this structure, allowing users to explore base-pair interactions in an intuitive graphical layout.

The application supports basic customization, such as temperature settings and optional structure constraints (if supported by the backend). Users can view both the text-based and 2D graphical representation of the structure. The visualization is rendered directly within the app, giving an immediate and interactive experience without needing desktop tools.

This project demonstrates full-stack integration, where the Flutter-based frontend communicates seamlessly with a Python backend API. It is a compact, modern alternative to traditional web tools, aimed at bringing RNA analysis to mobile platforms.

🔧 Tech Stack
Frontend: Flutter (Dart), Android Studio

Backend: Python (Flask or FastAPI), RNAfold / ViennaRNA

Visualization: Custom rendering or libraries for 2D RNA structure diagrams

📱 Features
RNA sequence input (manual or file)

Secondary structure prediction (via backend)

Dot-bracket and 2D visualization

Export and save results

Mobile-optimized UI

## Getting Started

This project is a starting point for a Flutter application.

A few resources to get you started if this is your first Flutter project:

- [Lab: Write your first Flutter app](https://docs.flutter.dev/get-started/codelab)
- [Cookbook: Useful Flutter samples](https://docs.flutter.dev/cookbook)

For help getting started with Flutter development, view the
[online documentation](https://docs.flutter.dev/), which offers tutorials,
samples, guidance on mobile development, and a full API reference.
