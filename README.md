After trying to edit a recording, and after finding (personal) success with my [video editor](https://github.com/dansgithubuser/dansvideoeditor), I've decided to make an audio editor in the same vein.

Audacity is the go-to free audio editing software. It's brilliant, open-source, and cross-platform. Yet, when a friend and I recorded something and tried to edit it, we were quickly bogged down trying to _re-edit_. Because Audacity does not record your edits themselves (other than a backward-only undo feature) it was hard to act on, say, a suggestion to put a section _back_ into the final result (or to even find where it was in the original, and where it belonged in the final).

Whereas Audacity treats the audio as the universe, in the context of editing, it seems clear to me that the edits themselves should be treated as the universe. The audio is a stateless input. If the edits are saved in a human-readable text format, then git can be used in conjunction and the result is a low-effort rich feature set for building edits.

Of course a sensible editor is still needed. It should output a human-readable edit instruction set and offer the user the following features:
- take sections of the original audio
- assemble sections into the final audio
- play back the final audio
- seek where to play the final audio from
- save and load edit instructions
- render to file

Some nice-to-haves:
- multiple original audio files
- adjust playback speed
- common filtering, such as compression
