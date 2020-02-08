After trying to edit a recording, and after finding (personal) success with my [video editor](https://github.com/dansgithubuser/dansvideoeditor), I've decided to make an audio editor in the same vein.

Audacity is the go-to free audio editing software. It's brilliant, open-source, and cross-platform. Yet, when a friend and I recorded something and tried to edit it, we were quickly bogged down trying to _re-edit_. Because Audacity does not record your edits themselves (other than a backward-only undo feature) it was hard to act on, say, a suggestion to put a section _back_ into the final result (or to even find where it was in the original, and where it belonged in the final).

Whereas Audacity treats the audio as the universe, in the context of editing, it seems clear to me that the edits themselves should be treated as the universe. The audio is a stateless input. If the edits are saved in a human-readable text format, then git can be used in conjunction and the result is a low-effort rich feature set for building edits.

Of course a sensible editor is still needed. It should output a human-readable edit instruction set and offer the user the following features:
- take sections of the original audio
- order sections as they will appear in the final audio
- play the final audio
- save and load edit instructions
- render to file

Some nice-to-haves:
- play original audio
- play section
- multiple original audio files
- adjust play speed
- common filtering, such as compression

## usage
### run
- `python dans-audio-editor` to start the server
- open `ui.html` in a browser

### starting
- to start editing a file, enter its full path
- to resume editing a file, enter the full path of the edit file
- the edit file path can be changed while editing

### flow
- first define a section by specifying its start, end, and name
- create an order of sections
- render the order (will be saved to `final-{now}.wav` in `dans-audio-editor`)
- click the play button to preview the render
