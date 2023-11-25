import {isArray} from "@bokehjs/core/util/types"
import {LayoutDOM, LayoutDOMView} from "@bokehjs/models/layouts/layout_dom"
import * as p from "@bokehjs/core/properties"

export function uuidv4() {
  return 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
    var r = Math.random() * 16 | 0, v = c == 'x' ? r : (r & 0x3 | 0x8);
    return v.toString(16);
  });
}

export function set_size(el: HTMLElement, model: HTMLBox, adjustMargin: boolean = true): void {
    let width_policy = model.width != null ? "fixed" : "fit"
    let height_policy = model.height != null ? "fixed" : "fit"
    const {sizing_mode, margin} = model
    if (sizing_mode != null) {
      if (sizing_mode == "fixed")
        width_policy = height_policy = "fixed"
      else if (sizing_mode == "stretch_both")
        width_policy = height_policy = "max"
      else if (sizing_mode == "stretch_width")
        width_policy = "max"
      else if (sizing_mode == "stretch_height")
        height_policy = "max"
      else {
        switch (sizing_mode) {
        case "scale_width":
          width_policy = "max"
          height_policy = "min"
          break
        case "scale_height":
          width_policy = "min"
          height_policy = "max"
          break
        case "scale_both":
          width_policy = "max"
          height_policy = "max"
          break
        default:
          throw new Error("unreachable")
        }
      }
    }
    let wm: number, hm: number
    if (!adjustMargin) {
      hm = wm = 0
    } else if (isArray(margin)) {
      if (margin.length === 4) {
        hm = margin[0] + margin[2]
        wm = margin[1] + margin[3]
      } else {
        hm = margin[0] * 2
        wm = margin[1] * 2
      }
    } else if (margin == null) {
      hm = wm = 0
    } else {
      wm = hm = margin * 2
    }
    if (width_policy == "fixed" && model.width)
      el.style.width = model.width + "px";
    else if (width_policy == "max")
      el.style.width = wm ? `calc(100% - ${wm}px)`: "100%";
    if (model.min_width != null)
      el.style.minWidth = model.min_width + "px";
    if (model.max_width != null)
      el.style.maxWidth = model.max_width + "px";
    if (height_policy == "fixed" && model.height)
      el.style.height = model.height + "px";
    else if (height_policy == "max")
      el.style.height = hm ? `calc(100% - ${hm}px)`: "100%";
    if (model.min_height != null)
      el.style.minHeight = model.min_height + "px";
    if (model.max_width != null)
      el.style.maxHeight = model.max_height + "px";
  }
  
  export abstract class HTMLBoxView extends LayoutDOMView {
    override model: HTMLBox
  
    render(): void {
      super.render()
      set_size(this.el, this.model)
    }
  
    get child_models(): LayoutDOM[] {
      return []
    }
  }
  
  export namespace HTMLBox {
    export type Attrs = p.AttrsOf<Props>
    export type Props = LayoutDOM.Props
  }
  
  export interface HTMLBox extends HTMLBox.Attrs {}
  
  export abstract class HTMLBox extends LayoutDOM {
    override properties: HTMLBox.Props
  
    constructor(attrs?: Partial<HTMLBox.Attrs>) {
      super(attrs)
    }
  }