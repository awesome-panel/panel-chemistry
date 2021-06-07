import * as p from "@bokehjs/core/properties"
import {HTMLBox, HTMLBoxView} from "@bokehjs/models/layouts/html_box"

export class NGLViewerView extends HTMLBoxView {
    model: NGLViewer
    _stage: any

    connect_signals(): void {
      super.connect_signals()
    //   this.connect(this.model.properties.config.change, this.render)
    }

    render(): void {
        super.render()
        this.el.id = "viewport"

        const wn = (window as any)
        const NGL = wn.NGL

        this._stage = new NGL.Stage(this.el);
        const stage = this._stage
        this.updateStage();
        window.addEventListener( "resize", function(){
            stage.handleResize();
        }, false );
        }

    after_layout(): void {
      super.after_layout()
      this._stage.handleResize();
    }

    updateStage(){
      this._stage.loadFile("rcsb://3UOG").then(function(o: any){
            o.addRepresentation("ribbon", {colorScheme: "chainid"});
            o.autoView();
          }
        )
    }
}

export namespace NGLViewer {
    export type Attrs = p.AttrsOf<Props>
    export type Props = HTMLBox.Props & {
        object: p.Property<string>,
        object_format: p.Property<string>,
        representation: p.Property<string>,
        color_scheme: p.Property<string>,
        spin: p.Property<boolean>,
    }
}

export interface NGLViewer extends NGLViewer.Attrs { }
export class NGLViewer extends HTMLBox {
    properties: NGLViewer.Props

    constructor(attrs?: Partial<NGLViewer.Attrs>) {
      super(attrs)
    }

    static __module__ = "panel_chemistry.bokeh_extensions.ngl_viewer"

    static init_NGLViewer(): void {
      this.prototype.default_view = NGLViewerView;

      this.define<NGLViewer.Props>(({ String, Boolean }) => ({
        object:             [ String, ""],
        object_format:             [ String, ""],
        representation:              [ String, ""],
        color_scheme:               [ String, ""],
        spin:               [ Boolean, false],
      }))

      this.override<NGLViewer.Props>({
        height: 400,
        width: 600
      });
    }
  }