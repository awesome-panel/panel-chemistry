import {LayoutDOM, LayoutDOMView} from "models/layouts/layout_dom"
import {LayoutItem} from "core/layout"
import * as p from "core/properties"

declare namespace NGL {
  class AtomProxy{

  }
  class Blob{
    constructor(list: Array<String>, ob: object)
  }
  class Colormaker{
    atomColor: (atom: AtomProxy) => string
  }

  class ColormakerRegistry{
    static addScheme(scheme: () => void) : String
    static addSelectionScheme(dataList: Array<Array<String>>, label: String): String
  }

  class Component{
    removeAllRepresentations(): void
    addRepresentation(type: String, params?: object) : RepresentationComponent
    reprList: RepresentationElement[]
  }

  class Matrix4{
    elements: Array<Number>
  }

  class RepresentationComponent{
  }

  class RepresentationElement{
    setParameters(params: any): this
    getParameters(): object
  }

  class Stage {
    compList: Array<Component>
    viewerControls: ViewerControls
    constructor(elementId: String, params?: object)
    loadFile(s: String| Blob, params?: object):  Promise<StructureComponent>
    autoView() : void
    setSpin(flag: Boolean): void
    removeAllComponents(type: String): void
    addRepresentation(representation: String): void
    handleResize(): void
  }

  class ScriptComponent{
    constructor(stage: Stage, params?: object)
    addRepresentation(type: String, params?: object) : RepresentationComponent
    autoView() : void
    removeAllRepresentations(): void
    reprList: RepresentationElement[]
  }

  class StructureComponent{
    constructor(stage: Stage, params?: object)
    addRepresentation(type: String, params?: object) : RepresentationComponent
    autoView() : void
    removeAllRepresentations(): void
    reprList: RepresentationElement[]
  }

  class SurfaceComponent{
    constructor(stage: Stage, params?: object)
    addRepresentation(type: String, params?: object) : RepresentationComponent
    autoView() : void
    removeAllRepresentations(): void
    reprList: RepresentationElement[]
  }



  class Vector3{
    x: number
    y: number
    z: number
  }

  class ViewerControls {
        position: Vector3
        Orientation: Matrix4
    }
}

export class NGLView extends LayoutDOMView {
  model: ngl
  public spin: Boolean
  public _stage: NGL.Stage

  initialize(): void {
    super.initialize()

    const url = "https://cdn.jsdelivr.net/gh/arose/ngl@v2.0.0-dev.37/dist/ngl.js"
    const script = document.createElement("script")
    script.onload = () => this._init()
    script.async = false
    script.src = url
    document.head.appendChild(script)
  }

  public set_variable_x(x: number): void {
    this._stage.viewerControls.position.x = x;
  }

  private _init(): void {

    //assign NGL viewer to the div of this class
    this.el.setAttribute('id','viewport')
    this._stage = new NGL.Stage('viewport')

    var m = this.model
    var stage = this._stage

    //initialize class with first values
    stage.loadFile( new Blob([m.pdb_string], {type: 'text/plain'}), { ext:'pdb'}).then(function (o) {
        o.addRepresentation(m.representation, { color: scheme })
        o.autoView()
    });
    var scheme = NGL.ColormakerRegistry.addSelectionScheme(m.color_list, "new scheme");


    stage.setSpin(m.spin)


    window.addEventListener( "resize", function(){
        stage.handleResize();
    }, false );

    //This section initiates the possible events that can be launched from the python side.
    //Each event has the name of an exported variable and should be launched whenever one
    //of these variables changes its value.

    //the spin event sets the spin to the current model.spin variable
    document.addEventListener('spin', function(){
       stage.setSpin(m.spin);
    });

    //the representation event removes the previous representation of the figure and adds the new representation in
    //model.representation
    document.addEventListener('representation', function(){
        stage.compList[0].removeAllRepresentations();
        stage.compList[0].addRepresentation(m.representation, { color: scheme })
    });

    //the rcsb_id event removes the current and loads a rcsb_id into the ngl_viewer
    document.addEventListener('rcsb_id', function(){
        stage.removeAllComponents("");
        stage.loadFile(m.rcsb_id).then(function (o) {
            o.addRepresentation(m.representation, { color: scheme })
            o.autoView()
        });
    });

    //the color_list event tries to update the colorlist of the current model, but if the list is badly defined,
    //the current colorscheme will persist. Note that the color_list is passed as an Any object, so it should first
    //be converted to an Array<Array<String>>
    document.addEventListener('color_list', function(){
        var list: Array<Array<String>> = m.color_list
        try{
              scheme = NGL.ColormakerRegistry.addSelectionScheme(list, "new scheme");
              stage.compList[0].reprList[0].setParameters( { color: scheme } );
        }
        catch(err) {
            console.log("badly defined color")
        }
    });

    //the pdb_string event removes the last model and loads in the new model from the pdb string
    document.addEventListener('pdb_string', function(){
        stage.removeAllComponents("");
        stage.loadFile( new Blob([m.pdb_string], {type: 'text/plain'}), { ext:'pdb'}).then(function (o) {
            o.addRepresentation(m.representation, { color: scheme })
            o.autoView()
        });

    });
   }

  get child_models(): LayoutDOM[] {
    return []
  }

  _update_layout(): void {
    this.layout = new LayoutItem()
    this.layout.set_sizing(this.box_sizing())
  }
}

export namespace ngl {
  export type Attrs = p.AttrsOf<Props>

  export type Props = LayoutDOM.Props & {
    spin: p.Property<boolean>
    representation: p.Property<string>
    rcsb_id: p.Property<string>
    color_list: p.Property<any>
    pdb_string: p.Property<string>
  }
}

export interface ngl extends ngl.Attrs {}

export class ngl extends LayoutDOM {
  properties: ngl.Props
  __view_type__: NGLView

  constructor(attrs?: Partial<ngl.Attrs>){
    super(attrs)
  }

  static __name__ = "ngl"

  static init_ngl() {
    // This is usually boilerplate. In some cases there may not be a view.
    this.prototype.default_view = NGLView

    this.define<ngl.Props>(({String, Boolean, Any}) => ({
      spin:             [Boolean, false],
      representation:   [String],
      rcsb_id:          [String],
      color_list:       [Any],
      pdb_string:       [String]
    })
    )
  }
}