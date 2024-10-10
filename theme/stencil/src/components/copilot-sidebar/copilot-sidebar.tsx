import { Component, h, Prop, State, Host } from '@stencil/core';
import {gb} from "../../util/util";

@Component({
  tag: 'copilot-sidebar',
  styleUrl: 'copilot-sidebar.css',
  shadow: false,
})
export class CopilotSidebar {
  // The copilotSrc is URL where the copilot sidebar is hosted
  @Prop()
  copilotSrc: string;

  @State()
  showSidebar = false;

  
  componentWillLoad() {
    this.showSidebar = gb.isOn('copilot-on-docs');
    gb.setRenderer(() => this.showSidebar = gb.isOn('copilot-on-docs'));
  }

render() {
    if (this.showSidebar === true) {
        return <Host>
          <aside id="ai-sidebar-target"></aside>
          <iframe id="ai-sidebar-host" src={this.copilotSrc}></iframe>
          </Host>;
    }else{
      return <Host></Host>;
    }

}

}
