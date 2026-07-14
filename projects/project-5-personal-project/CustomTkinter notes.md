# Parent Frames

For Tkinter (and CustomTkinter), the first argument to almost every widget is its parent, or master.

For example:
```py
frame = ctk.CTkFrame(app)
```
means: _"Create a frame whose parent is `app`"_

Then:
```py
label = ctk.CTkLabel(frame, text="Hello")
```
means: _"Create a label whose parent is `frame`"_

Visually we end up with 
```
App (root window)
│
├── ButtonFrame
│
├── DragAndDropFrame
│   ├── LabelText
│   │   ├── CTkLabel
│   │   ├── CTkLabel
│   │   └── CTkLabel
│   └── (other widgets)
│
└── CTkButton
```
Every widget belongs to another widget.

Thus, when writing:
```py
self.text_frame = LabelText(self, self.files)
```
inside `App`, `self` is the `App` object

You're saying _"Make `LabelText` a child of the main window"_

Instead if you write
```py
self.text_frame = LabelText(self.drop_frame, self.files)
```

You're saying _"Make `LabelText` live inside the drag-and-drop frame"_

This often makes more sense because the labels are displaying information that belongs to that frame.

## Why does every widget need a parent?
Tkinter needs to know:
* where to draw it
* what coordinates it uses
* what gets destroyed when the parent is destroyed
* how geometry managers (`grid`, `pack`, `place`) work

If you destroy the parent:
```py
self.drop_frame.destroy()
```
Everything inside disappears automatically

Think of widgets like folders
```
App/
│
├── ButtonFrame/
│   ├── Button
│   └── Button
│
└── DragAndDropFrame/
    ├── LabelText/
    │   ├── Label
    │   ├── Label
    │   └── Label
    └── TitleLabel
```
Each object "contains" its children.

**This is also why `self` changes**
One thing that is confusing when first learning is that `self` isn't always the same object.
Inside `App`
```py
class App:
  def __init__(self):
```
`self` is the App

Inside `DragAndDropFrame`
```py
class DragAndDropFrame:
  def on_drop(self, event):
```
`self` is the DragAndDropFrame

Inside `LabelText`
```py
class LabelText:
  def __init__(self, master, values):
```
`self` is the LabelText

So when you write
```py
LabelText(self.drop_frame, self.files)
```

you're passing one object (`self.drop_frame`) into the constructor of another object (`LabelText`) so it knows who its parent is.
