import * as PanelChemistryExtensions from "./bokeh_extensions/"
export {PanelChemistryExtensions}

import {register_models} from "@bokehjs/base"
register_models(PanelChemistryExtensions as any)