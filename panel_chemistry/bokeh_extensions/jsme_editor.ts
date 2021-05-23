// See https://docs.bokeh.org/en/latest/docs/reference/models/layouts.html
import { HTMLBox, HTMLBoxView } from "@bokehjs/models/layouts/html_box"

// See https://docs.bokeh.org/en/latest/docs/reference/core/properties.html
import * as p from "@bokehjs/core/properties"

// The view of the Bokeh extension/ HTML element
// Here you can define how to render the model as well as react to model changes or View events.
export class JSMEEditorView extends HTMLBoxView {
    model: JSMEEditor
    objectElement: any // Element

    connect_signals(): void {
        super.connect_signals()

        this.connect(this.model.properties.object.change, () => {
            this.render();
        })
    }

    render(): void {
        console.log("render")
        console.log(this.model)
        super.render()
        this.el.innerHTML = this.model.object
        this.objectElement = this.el.firstElementChild

        this.objectElement.addEventListener("click", () => {this.model.clicks+=1;}, false)
    }
}

export namespace JSMEEditor {
    export type Attrs = p.AttrsOf<Props>
    export type Props = HTMLBox.Props & {
        object: p.Property<string>,
        clicks: p.Property<number>,
    }
}

export interface JSMEEditor extends JSMEEditor.Attrs { }

// The Bokeh .ts model corresponding to the Bokeh .py model
export class JSMEEditor extends HTMLBox {
    properties: JSMEEditor.Props

    constructor(attrs?: Partial<JSMEEditor.Attrs>) {
        super(attrs)
    }

    static __module__ = "panel_chemistry.bokeh_extensions.jsme_editor"

    static init_JSMEEditor(): void {
        this.prototype.default_view = JSMEEditorView;

        this.define<JSMEEditor.Props>({
            object: [p.String, "<button style='width:100%'>Click Me</button>"],
            clicks: [p.Int, 0],
        })
    }
}