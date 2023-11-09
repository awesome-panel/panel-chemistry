// See https://docs.bokeh.org/en/latest/docs/reference/models/layouts.html
import { HTMLBox, HTMLBoxView } from "./layout"

// See https://docs.bokeh.org/en/latest/docs/reference/core/properties.html
import * as p from "@bokehjs/core/properties"
import {div} from "@bokehjs/core/dom"

function uuidv4() {
    return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
      var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
      return v.toString(16);
    });
  }

const notSubscribed = "Not Subscribed"

function readSDFValue(jsmeElement: any) {
    var data = jsmeElement.getMultiSDFstack();
    var output = "No multirecords SDF was pasted into the editor ";
    if (data.length > 0) {
        output = data.join("$$$$\n") + "$$$$\n";
    }
    return output;
}

function setModelValue(model: JSMEEditor, jsmeElement: any){
    console.log("setValue - start", model.value)
    var value = model.value
    if (model.format==="smiles"){
        console.log("getting smiles")
        value = jsmeElement.smiles()
        console.log("got smiles")
    } else if (model.format==="mol"){
        value = jsmeElement.molFile(false)
    } else if (model.format==="mol3000"){
        value = jsmeElement.molFile(true)
    } else if (model.format==="sdf"){
        value = readSDFValue(jsmeElement)
    } else {
        value = jsmeElement.jmeFile()
    }
    if (model.value!==value && value!==null){
        console.log("setting value", value)
        model.value = value
    }
    console.log("setValue - end", model.value)
}

function setModelValues(model: JSMEEditor, jsmeElement: any){
    console.log("setValues - start")
    setModelValue(model, jsmeElement)
    setOtherModelValues(model, jsmeElement)
    console.log("setValues - end")
}

function resetOtherModelValues(model: JSMEEditor, jsmeElement: any){
    if (!model.subscriptions.includes("jme")){model.jme = notSubscribed}
    if (!model.subscriptions.includes("smiles")){model.smiles = notSubscribed}
    if (!model.subscriptions.includes("mol")){model.mol = notSubscribed}
    if (!model.subscriptions.includes("mol3000")){model.mol3000 = notSubscribed}
    if (!model.subscriptions.includes("sdf")){model.sdf = notSubscribed}

    setModelValues(model, jsmeElement)
}

function cleanValue(value: any){
    if (value===null){
        return "null"
    } else {
        return value
    }
}

function setOtherModelValues(model: JSMEEditor, jsmeElement: any){
    console.log("setOtherValues - start")
    if (model.subscriptions.includes("jme")){model.jme = cleanValue(jsmeElement.jmeFile())}
    if (model.subscriptions.includes("smiles")){model.smiles = cleanValue(jsmeElement.smiles())}
    if (model.subscriptions.includes("mol")){model.mol = cleanValue(jsmeElement.molFile(false))}
    if (model.subscriptions.includes("mol3000")){model.mol3000 = cleanValue(jsmeElement.molFile(true))}
    if (model.subscriptions.includes("sdf")){model.sdf = cleanValue(readSDFValue(jsmeElement))}
    console.log("setOtherValues - end")
}

// The view of the Bokeh extension/ HTML element
// Here you can define how to render the model as well as react to model changes or View events.
export class JSMEEditorView extends HTMLBoxView {
    model: JSMEEditor
    jsmeElement: any // Element
    JSME = (window as any).JSApplet.JSME
    valueFunc: any
    valueChanging: boolean = true
    container: HTMLDivElement

    initialize(): void {
        super.initialize()
        this.container = div({
          style: {display: "contents"}
        })
    }

    connect_signals(): void {
        super.connect_signals()

        this.connect(this.model.properties.value.change, () => {
            console.log("value change", this.model.value)
            if (!this.valueChanging){
                if (this.model.value===""){
                    this.jsmeElement.reset()
                } else {
                    this.jsmeElement.readGenericMolecularInput(this.model.value)
                }
            }
        })
        this.connect(this.model.properties.format.change, () => {
            console.log("format change", this.model.format)
            setModelValue(this.model, this.jsmeElement);
        })
        this.connect(this.model.properties.subscriptions.change, () => {
            console.log("subscriptions change", this.model.subscriptions)
            resetOtherModelValues(this.model, this.jsmeElement);
        })
        this.connect(this.model.properties.options.change, () => {
            console.log("options change", this.model.options)
            this.setJSMEOptions()
        })
        this.connect(this.model.properties.guicolor.change, () => {
            console.log("options change", this.model.options)
            this.setGUIColor()
        })
    }

    render(): void {
        console.log("render - start")
        super.render()
        const id = "jsme-" + uuidv4()
        const el = div({
          class: "jsme-editor",
          id: id,
          style: {width: "100%", height: "100%"}
        })
        this.container.appendChild(el)

        // wait for DOM to be updated
        setTimeout(() => { this.createJSMEElement() }, 200);
    }

    createJSMEElement() {
        const id = this.container.children[0].id

        // Need to add it to document body for JSME to be able to find the id
        document.body.appendChild(this.container)

        this.jsmeElement = new this.JSME(id, this.getHeight(), this.getWidth(), {
            "options": this.model.options.join(","),
            "guicolor": this.model.guicolor
        });
        this.jsmeElement.readGenericMolecularInput(this.model.value)
        resetOtherModelValues(this.model, this.jsmeElement)
        setModelValues(this.model, this.jsmeElement)

        const this_ = this;
        function showEvent(event: any){
            console.log("event", event)
            this_.valueChanging = true
            setModelValues(this_.model, this_.jsmeElement)
            this_.valueChanging = false
        }
        this.jsmeElement.setAfterStructureModifiedCallback(showEvent);

        // Remove from document body and add to shadow DOM
        document.body.removeChild(this.container)
        this.shadow_el.appendChild(this.container)

        console.log("render - end")
    }

    setGUIColor(){
        console.log("setGUIColor", this.model.guicolor)
        this.jsmeElement.setUserInterfaceBackgroundColor(this.model.guicolor)
    }

    setJSMEOptions(){
        const options = this.model.options.join(",")
        console.log("setJSMEOptions", options)
        this.jsmeElement.options(options)
    }

    getHeight(){
        if ((this.model.sizing_mode==="stretch_height" || this.model.sizing_mode==="stretch_both") && this.el.style.height){
            return this.el.style.height
        }
        else if (this.model.height){
            return this.model.height.toString() + "px"
        } else  {
            return "100px"
        }
    }
    getWidth(){
        if ((this.model.sizing_mode==="stretch_width" || this.model.sizing_mode==="stretch_both") && this.el.style.width){
            return this.el.style.width
        }
        else if (this.model.width){
            return this.model.width.toString() + "px"
        } else  {
            return "100px"
        }
    }

    resizeJSMEElement() {
        if (this.jsmeElement !== undefined) {
            this.jsmeElement.setSize(this.getWidth(), this.getHeight());
        }
    }

    after_layout(): void{
        super.after_layout()
        this.resizeJSMEElement()
    }
}

export namespace JSMEEditor {
    export type Attrs = p.AttrsOf<Props>
    export type Props = HTMLBox.Props & {
        value: p.Property<string>,
        format: p.Property<string>,
        options: p.Property<string[]>

        jme: p.Property<string>,
        smiles: p.Property<string>,
        mol: p.Property<string>,
        mol3000: p.Property<string>,
        sdf: p.Property<string>,

        subscriptions: p.Property<string[]>

        guicolor: p.Property<string>,
    }
}

export interface JSMEEditor extends JSMEEditor.Attrs { }

// The Bokeh .ts model corresponding to the Bokeh .py model
export class JSMEEditor extends HTMLBox {
    properties: JSMEEditor.Props
    __view_type__: JSMEEditorView

    constructor(attrs?: Partial<JSMEEditor.Attrs>) {
        super(attrs)
    }

    static __module__ = "panel_chemistry.bokeh_extensions.jsme_editor"

    static {
        this.prototype.default_view = JSMEEditorView;

        this.define<JSMEEditor.Props>(({String, Array}) => ({
            value: [String, "N[C@@H](CCC(=O)N[C@@H](CS)C(=O)NCC(=O)O)C(=O)O"],
            format: [String, ""],
            options: [ Array(String),   [] ],
            jme: [String, ""],
            smiles: [String, ""],
            mol: [String, ""],
            mol3000: [String, ""],
            sdf: [String, ""],
            subscriptions: [ Array(String),   [] ],
            guicolor: [String, "#c0c0c0"],
        }))
    }
}
