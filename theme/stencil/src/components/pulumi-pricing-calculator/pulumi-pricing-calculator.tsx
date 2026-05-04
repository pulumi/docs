import { Component, State, h } from '@stencil/core';

type Duration = "day" | "month";

@Component({
  tag: 'pulumi-pricing-calculator',
  styleUrl: 'pulumi-pricing-calculator.scss',
  shadow: false,
})

export class PulumiPricingCalculator {
  @State()
  duration: Duration = "month"

  @State()
  resourceCount: number = 500;

  @State()
  utilization: number = 100;

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
    return 3000;
  }

  getEstimatedDeploymentMinutes() {
    return this.deploymentMinutes * 30;
  }

  updateDeploymentsExpanded() {
    this.deploymentsExpanded = !this.deploymentsExpanded
  }

  getEstimatedCredits() {
    // Calculate credits based on resource count and utilization
    // This represents the actual resource hours used
      return this.resourceCount * (24 * (this.utilization / 100)) * 30;
  }

  getFreeCredits() {
    // Free credits represent the base rate coverage
    // For 500 resources at 100% utilization = 500 * 24 * 30 = 360,000 credits
    return 500 * 24 * 30;
  }

  getCostPerCredit() {
    // $0.1825 per additional resource per month
    // For 1 additional resource at 100% utilization = 1 * 24 * 30 = 720 credits
    // So cost per credit = $0.1825 / 720 = $0.000253472...
    return 0.000253472;
  }

  getTotal() {
    // IaC cost
    const additionalCredits = Math.max(0, this.getEstimatedCredits() - this.getFreeCredits());
    const additionalCost = additionalCredits * this.getCostPerCredit();
    let totalCost = 40 + additionalCost;

    // Add on Pulumi Deployments cost
    if (this.deploymentsExpanded) {
        const deploymentCost = ((this.getEstimatedDeploymentMinutes() - this.getFreeDeploymentMinutes()) * this.getCostPerDeploymentMinute());
        totalCost = totalCost + (deploymentCost > 0 ? deploymentCost : 0);
    } 

    totalCost = totalCost > 40 ? totalCost : 40;

    return this.duration == "month" ? totalCost : totalCost / 30.0;
  }

  isTotalOverMax() {
    return this.getTotal() > 1670 && this.duration === "month" || this.getTotal() > 55 && this.duration === "day";
  }

  showFormattedTotal() {
    const total = this.getTotal();
    return `$${total.toFixed(2)} USD / ${this.duration === "day" ? "day" : "mon"}`
  }

  updateResourceCount(event: CustomEvent) {
    const val = (event.target as HTMLInputElement).value.trim();
    this.resourceCount = val === "" ? 0 : parseInt(val)
  }

  updateUtilization(event: CustomEvent) {
    const val = (event.target as HTMLInputElement).value.trim();
    this.utilization = val === "" ? 1 : parseInt(val)
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
      <div class="calculator">
        <h3>IaC Cost estimator</h3>
        <div class="edition">Team Edition</div>
        <div class="content">
          <div class="inputs">
              <div class="field">
                  <div class="title">Number of resources</div>
                  <div class="details">
                      <div class="description">
                          All cloud resources cost the same amount in Pulumi Cloud. Look at your cloud account and enter
                          here the number of
                          resources.
                      </div>
                      <div class="input">
                          <input class="resource-count" type="number" min="0" onInput={event=>
                          this.updateResourceCount(event as any)} value={this.resourceCount}
                          ></input>
                      </div>
                  </div>
              </div>

              <div class="field">
                  <div class="title">Utilization</div>
                  <div class="details">
                      <div class="description">
                          If you have resources that are being spun up and down throughout the day, estimate the
                          percentage of the time the total
                          resource count will be reached.
                      </div>
                      <div class="utilization">
                          <div class="input">
                              <input type="number" min="1" max="100" onInput={event=> this.updateUtilization(event as
                              any)} value={this.utilization}></input><span class="percent">%</span>
                          </div>
                          <input type="range" min="1" max="100" step="1" onInput={event=> this.updateUtilization(event as
                          any)} value={this.utilization} class="range purple" />
                      </div>
                  </div>
              </div>

              <div class={this.deploymentsExpanded ? "deployments" : "deployments collapsed" }>
                  <div class="default">
                      <svg xmlns="http://www.w3.org/2000/svg" class="ph-icon ph-icon--regular" fill="currentColor" viewBox="0 0 256 256" aria-hidden="true" focusable="false">
                          <path d="M223.85,47.12a16,16,0,0,0-15-15c-12.58-.75-44.73.4-71.41,27.07L132.69,64H74.36A15.91,15.91,0,0,0,63,68.68L28.7,103a16,16,0,0,0,9.07,27.16l38.47,5.37,44.21,44.21,5.37,38.49a15.94,15.94,0,0,0,10.78,12.92,16.11,16.11,0,0,0,5.1.83A15.91,15.91,0,0,0,153,227.3L187.32,193A15.91,15.91,0,0,0,192,181.64V123.31l4.77-4.77C223.45,91.86,224.6,59.71,223.85,47.12ZM74.36,80h42.33L77.16,119.52,40,114.34Zm74.41-9.45a76.65,76.65,0,0,1,59.11-22.47,76.46,76.46,0,0,1-22.42,59.16L128,164.68,91.32,128ZM176,181.64,141.67,216l-5.19-37.17L176,139.31Zm-74.16,9.5C97.34,201,82.29,224,40,224a8,8,0,0,1-8-8c0-42.29,23-57.34,32.86-61.85a8,8,0,0,1,6.64,14.56c-6.43,2.93-20.62,12.36-23.12,38.91,26.55-2.5,36-16.69,38.91-23.12a8,8,0,1,1,14.56,6.64Z"/>
                      </svg>
                      <div class="details">
                          <div class="title">Add on Pulumi Deployments</div>
                          <div class="subtitle">Run deployments remotely with a button, Git push, or REST API</div>
                      </div>
                      <button onClick={()=> this.updateDeploymentsExpanded()}>
                          {this.deploymentsExpanded ? (
                              <svg xmlns="http://www.w3.org/2000/svg" class="ph-icon ph-icon--regular" fill="currentColor" viewBox="0 0 256 256" aria-hidden="true" focusable="false"><path d="M224,128a8,8,0,0,1-8,8H40a8,8,0,0,1,0-16H216A8,8,0,0,1,224,128Z"/></svg>
                          ) : (
                              <svg xmlns="http://www.w3.org/2000/svg" class="ph-icon ph-icon--regular" fill="currentColor" viewBox="0 0 256 256" aria-hidden="true" focusable="false"><path d="M224,128a8,8,0,0,1-8,8H136v80a8,8,0,0,1-16,0V136H40a8,8,0,0,1,0-16h80V40a8,8,0,0,1,16,0v80h80A8,8,0,0,1,224,128Z"/></svg>
                          )}
                      </button>
                  </div>


                  <div class={ this.deploymentsExpanded ? "field visible" : "field" }>
                      <div class="title">Deployment minutes per day</div>
                      <div class="details">
                          <div class="description">
                              Deployment minutes refer to the duration of time elapsed when running deployments on
                              Pulumi’s compute. Use your current update times and add buffer for any workflows that need
                              to happen.
                          </div>
                          <div class="input">
                              <input type="number" min="0" onInput={event=> this.updateDeploymentMinutes(event as any)}
                              value={this.deploymentMinutes}></input>
                          </div>
                      </div>
                  </div>
              </div>
          </div>
          <div class="outputs">
            <div class="gradient"></div>
            <div class="contents">
                <div class="duration">
                    <button class={ this.duration==='day' ? 'active' : null} onClick={()=>
                        this.updateDuration("day")}>Per day</button>
                    <button class={ this.duration==='month' ? 'active' : null} onClick={()=>
                        this.updateDuration("month")}>Per month</button>
                </div>
                <div class="items">
                    <div class="item"><span>Estimated credits per {this.duration}</span><span>{
                            this.formatNumber(this.getEstimatedCredits())}</span></div>
                    <div class="item"><span>Free credits
                            included</span><span>{this.formatNumber(this.getFreeCredits())}</span></div>
                    <div class="item"><span>Cost per credit</span><span>${this.getCostPerCredit().toFixed(5)}</span></div>

                    <div class={ this.deploymentsExpanded ? "deployment-total visible" : "deployment-total" }>
                        <div class="subtitle">Deployments</div>
                        <div class="item"><span>Estimated deployment minutes per {this.duration}</span><span>{
                            this.formatNumber(this.getEstimatedDeploymentMinutes())}</span></div>
                        <div class="item"><span>Deployment minutes
                                included</span><span>{this.formatNumber(this.getFreeDeploymentMinutes())}</span></div>
                        <div class="item"><span>Cost per deployment
                                minute</span><span>${this.getCostPerDeploymentMinute()}</span></div>
                    </div>
                </div>
                <div class="divider"></div>
                <div class={this.isTotalOverMax() ? 'total over-max' : 'total'}>
                    <span class="contact"><a href="/contact/?form=sales">Contact sales</a>for bulk discounts</span>
                    <span class={this.isTotalOverMax() ? 'blurred' : ''}>{this.showFormattedTotal()}</span>
                </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
