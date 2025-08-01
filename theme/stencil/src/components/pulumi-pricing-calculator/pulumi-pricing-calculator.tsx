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
                      <i class="fas fa-rocket"></i>
                      <div class="details">
                          <div class="title">Add on Pulumi Deployments</div>
                          <div class="subtitle">Run deployments remotely with a button, Git push, or REST API</div>
                      </div>
                      <button onClick={()=> this.updateDeploymentsExpanded()}><i class={this.deploymentsExpanded
                              ? "fas fa-minus" : "fas fa-plus" }></i></button>
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
