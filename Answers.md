```C
// snekobject.c
#include "snekobject.h"

void snek_object_free(snek_object_t *obj) {
  switch (obj->kind) {
  case INTEGER:
  case FLOAT:
    break;
  case STRING:
    free(obj->data.v_string);
    break;
  case VECTOR3:
    break;
  case ARRAY: 
    free(obj->data.v_array.elements);
    break;
  }
  free(obj);
}

// vm.c
#include "vm.h"
#include "stack.h"

void vm_free(vm_t *vm) {
  for (int i = 0; i < vm->frames->capacity; i++) {
    stack_free(vm->frames);
    for (int j = 0; j < vm->objects->capacity; j++) {
      snek_object_free(vm->objects);
      stack_free(vm->objects);
      free(vm);
    }
  }
}

// don't touch below this line

vm_t *vm_new() {
  vm_t *vm = malloc(sizeof(vm_t));
  if (vm == NULL) {
    return NULL;
  }

  vm->frames = stack_new(8);
  vm->objects = stack_new(8);
  return vm;
}

void vm_track_object(vm_t *vm, snek_object_t *obj) {
  stack_push(vm->objects, obj);
}

void vm_frame_push(vm_t *vm, frame_t *frame) { stack_push(vm->frames, frame); }

frame_t *vm_new_frame(vm_t *vm) {
  frame_t *frame = malloc(sizeof(frame_t));
  frame->references = stack_new(8);

  vm_frame_push(vm, frame);
  return frame;
}

void frame_free(frame_t *frame) {
  stack_free(frame->references);
  free(frame);
}

```

```py

import customtkinter as ctk
import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD


class App(TkinterDnD.Tk):
    def __init__(self):
        super().__init__()

        ctk.set_appearance_mode("System")
        ctk.set_default_color_theme("blue")

        self.files = []  # <-- shared state for left buttons

        # Root layout
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Left frame (buttons)
        self.left = ctk.CTkFrame(self, corner_radius=10)
        self.left.grid(row=0, column=0, sticky="ns", padx=10, pady=10)

        ctk.CTkButton(self.left, text="Act on files", command=self.act_on_files).pack(
            padx=10, pady=10
        )

        # Right frame (drop area)
        self.drop_area = ctk.CTkFrame(self, corner_radius=10)
        self.drop_area.grid(row=0, column=1, sticky="nsew", padx=10, pady=10)

        self.drop_label = ctk.CTkLabel(
            self.drop_area, text="Drag files here", font=ctk.CTkFont(size=16, weight="bold")
        )
        self.drop_label.pack(expand=True, fill="both", padx=20, pady=20)

        # Make CTkFrame accept drops
        self.drop_area.drop_target_register(DND_FILES)
        self.drop_area.dnd_bind("<<Drop>>", self.on_files_dropped)

    def on_files_dropped(self, event):
        # event.data is usually a string containing one or more file paths
        # wrapped in braces if they contain spaces.
        raw = event.data

        # tkinterdnd2 common parsing approach:
        paths = self._parse_dnd_files(raw)

        self.files = paths
        self.drop_label.configure(text=f"Dropped {len(self.files)} file(s)")

        # optional: print for debugging
        print("Dropped:", self.files)

    def act_on_files(self):
        if not self.files:
            self.drop_label.configure(text="Drop files first")
            return

        # Do something with self.files
        # e.g., process each file
        print("Acting on:", self.files)

    def _parse_dnd_files(self, raw):
        raw = raw.strip()

        # If there's only one file without braces/spaces, this often works:
        if raw.startswith("{") is False and raw.count(" ") == 0 and raw.count("\n") == 0:
            return [raw]

        # Parse "{path with spaces} {path2} ..."
        out = []
        cur = ""
        in_braces = False

        for ch in raw:
            if ch == "{":
                in_braces = True
                continue
            if ch == "}":
                in_braces = False
                out.append(cur)
                cur = ""
                continue

            if ch == " " and not in_braces:
                if cur:
                    out.append(cur)
                    cur = ""
                continue

            cur += ch

        if cur:
            out.append(cur)

        return out


if __name__ == "__main__":
    app = App()
    app.mainloop()

```
```py
import customtkinter as ctk
from tkinterdnd2 import DND_FILES, TkinterDnD

class TopLevelWindow(ctk.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.geometry("400x300")

        self.label = ctk.CTkLabel(self, text="TopLevelWindow")
        self.label.pack(padx=20, pady=20)

class DragAndDropFrame(ctk.CTkFrame):
    def __init__(self, master, title):
        super().__init__(master)

        self.grid_columnconfigure(0, weight=1)
        self.title = title

        self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")



class ButtonFrame(ctk.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.buttons = []

        self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            button = ctk.CTkButton(self, text=value)
            button.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="ew")

class CheckBoxFrame(ctk.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.checkboxes = []

        self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            checkbox = ctk.CTkCheckBox(self, text=value)
            checkbox.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self) -> str:
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes

class RadiobuttonFrame(ctk.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.title = title
        self.radiobuttons = []
        self.variable = ctk.StringVar(value="")

        self.title = ctk.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            radiobutton = ctk.CTkRadioButton(self, text=value, value=value, variable=self.variable)
            radiobutton.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.radiobuttons.append(radiobutton)

    def get(self) -> str:
        return self.variable.get()

    def set(self, value) -> None:
        self.variable.set(value)

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("App title goes here")
        self.geometry("400x380")
        self.grid_columnconfigure((0, 1), weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.toplevel_window = None

        self.button = ctk.CTkButton(self, text="New window", command=self.create_toplevel_window)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

        self.button_frame = ButtonFrame(self, "Functions", values=["QR Code", "Something else"])
        self.button_frame.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nsw")

        self.drop_frame = DragAndDropFrame(self, "File")
        self.drop_frame.grid(row=0, column=1, padx=(0,10), pady=(10,0), sticky="nsew")
        self.drop_frame.configure(fg_color="transparent")

    # Figure out how to inject this to the frame to capture data.
        def on_drop(event) -> str:
            files = self.drop_frame.tk.splitlist(event.data)
            entry.delete(0, "end")
            entry.insert(0, files[0])

        TkinterDnD.require(self.drop_frame)
        entry = ctk.CTkEntry(
            self.drop_frame, width=200, placeholder_text="Drag file here..."
        )

        entry.drop_target_register(DND_FILES)
        entry.dnd_bind("<<Drop>>", on_drop)

    def button_callback(self) -> None:
        print("checked checkboxes", self.checkbox_frame.get())
        print("radiobutton_frame", self.radiobutton_frame.get())

    def create_toplevel_window(self) -> None:
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = TopLevelWindow(self)
        else:
            self.toplevel_window.focus()
```
