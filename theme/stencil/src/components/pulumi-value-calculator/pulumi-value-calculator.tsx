import { Component, State, h } from '@stencil/core';

@Component({
  tag: 'pulumi-value-calculator',
  styleUrl: 'pulumi-value-calculator.scss',
  shadow: false,
})

export class PulumiPricingCalculator {
  @State()
  devCount: number = 5;

  @State()
  devSalary: number = 138000

  @State()
  devTime: number = 20

  @State()
  assumptionsExpanded: boolean = false;

  updateAssumptionsExpanded() {
    this.assumptionsExpanded = !this.assumptionsExpanded
  }

  getDevCost() {
    return (this.devCount * this.devSalary * this.devTime) / 100;
  }

  getPulumiCost() {
    if (this.devCount < 50) {
        return this.devCount * 8046;
    } else if (this.devCount >= 50 && this.devCount < 100) {
        return this.devCount * 3129;
    } else if (this.devCount >= 100) {
        return this.devCount * 1266;
    }
  }

  updateDevCount(event: CustomEvent) {
    const val = (event.target as HTMLInputElement).value.trim();
    this.devCount = val === "" ? 5 : parseInt(val);
  }

  updateDevSalary(event: CustomEvent) {
    const val = (event.target as HTMLInputElement).value.trim();
    this.devSalary = val === "" ? 138000 : parseInt(val);
  }

  updateDevTime(event: CustomEvent) {
    const val = (event.target as HTMLInputElement).value.trim();
    this.devTime = val === "" ? 20 : parseInt(val);
  }

  formatNumber(num: number) {
    return new Intl.NumberFormat().format(Math.round(num));
  }

  getTotal() {
    const total = this.getDevCost() - this.getPulumiCost();
    return total;
  }

  showFormattedTotal() {
    return `$${this.formatNumber(this.getTotal())} USD`
  }

  render() {
    return (
        <div class="value-calculator">
            <h3>Platform Engineering ROI Estimator</h3>
            <h5>Improve your cloud ROI by unleashing developer productivity</h5>
            <div class="main-content">
                <div class="field">
                    <div class="details">
                        <div class="info-side">
                            <div class="title">How many developers are in your company?</div>
                            <div class="input">
                                <input type="number" min="5" max="250" readOnly value={this.devCount}/>
                            </div>
                        </div>
                        <div class="slider-side">
                            <input type="range" min="5" max="250" step="5" onInput={event => this.updateDevCount(event as any)} value={this.devCount} class="range purple w-full"/>
                            <div class="w-full flex flex-row ticks"></div>
                        </div>
                    </div>
                </div>
                <div class="field">
                    <div class="details">
                        <div class="info-side content-center">
                            <div class="title">Your estimated annual developer cost savings* are:</div>
                        </div>
                        <div class="rainbow-text">{this.showFormattedTotal()}</div>
                    </div>
                </div>
                <div class={this.assumptionsExpanded ? "assumptions" : " assumptions collapsed" }>
                    <div class="default justify-between">
                        <div class="subtitle">*Based on industry averages of developer salaries and the time spent managing cloud infrastructure. Adjust these assumptions here.</div>
                        <button onClick={()=> this.updateAssumptionsExpanded()}><i class={this.assumptionsExpanded ? "fas fa-minus" : "fas fa-plus" }></i></button>
                    </div>
                    <div class={ this.assumptionsExpanded ? "field visible" : "field" }>
                        <div class="details">
                            <div class="info-side">
                                <div class="title">What is the average developer salary in your company?</div>
                                <div class="description">US National average is $138K</div>
                                <div class="input">
                                    <input type="number" readOnly value={this.devSalary}></input>
                                </div>
                            </div>
                            <div class="slider-side content-center">
                                <input type="range" min="85000" max="200000" step="5" onInput={event => this.updateDevSalary(event as any)} value={this.devSalary} class="range purple w-full"/>
                                <div class="w-full flex flex-row ticks"></div>
                            </div>
                        </div>
                        <div class="details">
                            <div class="info-side">
                                <div class="title">How much time do these developers spend managing cloud infrastructure?</div>
                                <div class="description">Average is 20%</div>
                                <div class="input">
                                    <input type="number" readOnly value={this.devTime}></input><span class="percent">%</span>
                                </div>
                            </div>
                            <div class="slider-side content-center">
                                <input type="range" min="10" max="100" step="1" onInput={event => this.updateDevTime(event as any)} value={this.devTime} class="range purple w-full"/>
                                <div class="w-full flex flex-row ticks"></div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    );
  }
}
