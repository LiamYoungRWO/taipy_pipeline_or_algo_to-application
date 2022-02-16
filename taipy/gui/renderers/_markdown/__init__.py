from typing import Any

from markdown.extensions import Extension

from .blocproc import StartBlockProcessor
from .control import ControlPattern
from .postproc import Postprocessor
from .preproc import Preprocessor

class TaipyMarkdownExtension(Extension):
    
    config = {"gui" : ["", "Gui object for extension"]}

    def extendMarkdown(self, md):
        md.registerExtension(self)
        # md.preprocessors.add("taipy", Preprocessor(md), "_begin")
        md.preprocessors.register(Preprocessor(md), "taipy", 210)
        ControlPattern.extendMarkdown(md)
        md.parser.blockprocessors.register(
            StartBlockProcessor(md.parser), "taipy", 175
        )  # process the block tags (layout and co)
        md.treeprocessors.register(Postprocessor(md), "taipy", 200)
        print(self.config["gui"][0])