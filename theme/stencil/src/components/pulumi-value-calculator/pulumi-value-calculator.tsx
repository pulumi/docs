import { Component, State, h } from '@stencil/core';

type Duration = "day" | "month";

@Component({
  tag: 'pulumi-value-calculator',
  styleUrl: 'pulumi-value-calculator.scss',
  shadow: false,
})

export class PulumiPricingCalculator {
  @State()
  duration: Duration = "month"

  @State()
  resourceCount: number = 500;

  @State()
  devCount: number = 5;

  @State()
  deploymentsExpanded: boolean = false;

  @State()
  deploymentMinutes: number = 0;

  updateDuration(duration: Duration) {
      this.duration = duration;
  }

  getCostPerDeploymentMinute() {
      return 0.01;
  }

  getFreeDeploymentMinutes() {
    if (this.duration === "month") {
        return 3000;
    } else {
        return (3000 / 30);
    }
  }

  getEstimatedCredits() {
    if (this.duration === "month") {
        return this.resourceCount * (24 * (this.devCount / 100)) * 30
    } else {
        return this.resourceCount * (24 * (this.devCount / 100))
    }
  }

  getEstimatedDeploymentMinutes() {
    if (this.duration === "month") {
        return this.deploymentMinutes * 30;
    } else {
        return this.deploymentMinutes;
    }
  }

  updateDeploymentsExpanded() {
    this.deploymentsExpanded = !this.deploymentsExpanded
  }

  getFreeCredits() {
    if (this.duration === "month") {
        return 150000;
    } else {
        return (150000 / 30);
    }
  }

  getCostPerCredit() {
    return 0.0005;
  }

  getTotal() {
    if (this.deploymentsExpanded) {
        const deploymentCost = ((this.getEstimatedDeploymentMinutes() - this.getFreeDeploymentMinutes()) * this.getCostPerDeploymentMinute());
        const cost = ((this.getEstimatedCredits() - this.getFreeCredits()) * this.getCostPerCredit()) + (deploymentCost > 0 ? deploymentCost : 0);
        return cost > 0 ? cost : 0;
    } else {
        const cost = (this.getEstimatedCredits() - this.getFreeCredits()) * this.getCostPerCredit();
        return cost > 0 ? cost : 0;
    }
  }

  isTotalOverMax() {
    return this.getTotal() > 1670 && this.duration === "month" || this.getTotal() > 55 && this.duration === "day";
  }

  showFormattedTotal() {
    return `$${this.formatNumber(this.getTotal())} USD`
  }

  updateResourceCount(event: CustomEvent) {
    const val = (event.target as HTMLInputElement).value.trim();
    this.resourceCount = val === "" ? 0 : parseInt(val)
  }

  updateDevCount(event: CustomEvent) {
    const val = (event.target as HTMLInputElement).value.trim();
    this.devCount = val === "" ? 1 : parseInt(val)
  }

  updateDeploymentMinutes(event: CustomEvent) {
    const val = (event.target as HTMLInputElement).value.trim();
    this.deploymentMinutes = val === "" ? 0 : parseInt(val)
  }

  formatNumber(num: number) {
    return new Intl.NumberFormat().format(Math.round(num));
  }

  render() {
    return (
      <div class="value-calculator">
        <h3>Platform Engineering ROI Calculator</h3>
        <h5>Improve your cloud ROI by unleashing developer productivity</h5>
        <div class="main-content">
            <div class="field">
                <div class="info-side">
                    <div class="title">How many developers are in your company?</div>
                    <div class="input">
                        <input type="number" min="5" max="5000" onInput={event => this.updateDevCount(event as any)} value={this.devCount}/>
                    </div>
                </div>
                <div class="slider-side">
                    <input type="range" min="5" max="5000" step="5" onInput={event => this.updateDevCount(event as any)} value={this.devCount} class="range purple w-full"/>
                    <div class="w-full flex flex-row ticks"></div>
                </div>
            </div>
            <div class="field">
                <div class="info-side content-center">
                    <div class="title">Your estimated annual developer cost savings* are:</div>
                </div>
                <div class="rainbow-text">{this.showFormattedTotal()}</div>
            </div>
            <a class={this.deploymentsExpanded ? "deployments" : " deployments collapsed" }>
                  <div class="default justify-between">
                        <div class="subtitle">*Based on industry averages of developer salaries and the time spent managing cloud infrastructure. Adjust these assumptions here.</div>
                      <button onClick={()=> this.updateDeploymentsExpanded()}><i class={this.deploymentsExpanded
                              ? "fas fa-minus" : "fas fa-plus" }></i></button>
                  </div>
                  <div class={ this.deploymentsExpanded ? "field visible" : "field" }>
                      <div class="title">What is the average developer salary in your company?</div>
                      <div class="details">
                          <div class="description">
                              US National average is $138K
                          </div>
                          <div class="input">
                              <input type="number" min="0" onInput={event=> this.updateDeploymentMinutes(event as any)}
                              value={this.deploymentMinutes}></input>
                          </div>
                      </div>
                      <div class="title">How much time to these developers spend managing cloud infrastructure?</div>
                      <div class="details">
                          <div class="description">
                              Average is 20%
                          </div>
                          <div class="input">
                              <input type="number" min="0" onInput={event=> this.updateDeploymentMinutes(event as any)}
                              value={this.deploymentMinutes}></input>
                          </div>
                      </div>
                  </div>
              </a>
        </div>
      </div>
    );
  }
}
