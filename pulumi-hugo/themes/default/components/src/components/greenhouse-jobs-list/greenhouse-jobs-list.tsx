import { Component, h, State } from '@stencil/core';

interface GreenhouseJob {
    id: number;
    title: string;
    absolute_url: string;
    location: {
        name: string;
    };
}

interface GreenhouseJobDepartment {
    id: number;
    name: string;
    jobs: GreenhouseJob[],
}

@Component({
    tag: "pulumi-greenhouse-jobs-list",
    shadow: false,
})
export class GreenhouseJobsList {

    @State()
    departments: GreenhouseJobDepartment[];

    @State()
    loading: boolean;

    constructor() {
        this.departments = []
    }

    componentWillLoad() {
        this.fetchJobs();
    }

    async fetchJobs() {
        this.loading = true;

        // There are a few different ways to fetch data from Greenhouse, but by department is most
        // convenient, since it returns a list of jobs along with each department.
        // https://developers.greenhouse.io/job-board.html
        try {
            const response = await fetch("https://boards-api.greenhouse.io/v1/boards/pulumicorporation/departments");
            const data = await response.json();

            if (data && data.departments) {
                this.departments = data.departments
                    // Only include departments that have open positions.
                    .filter((department: GreenhouseJobDepartment) => department.jobs.length > 0);
            }
        } catch (error) {
            console.error(error);
        }

        this.loading = false;
    }

    renderLoadingSpinner() {
        return <div class="loading-spinner"></div>;
    }

    renderJobsList() {
        return this.departments.length > 0 ?
            <ul class="departments">
                {
                    this.departments.map(department => <li>
                        <h4>{department.name}</h4>
                        <ul class="jobs">
                            {
                                department.jobs.map(job => <li>
                                    <a class="job-title" href={job.absolute_url} target="_blank" rel="noreferrer noopener">
                                        {job.title}
                                    </a>
                                    <div class="job-location">
                                        {job.location.name}
                                    </div>
                                </li>)
                            }
                        </ul>
                    </li>)
                }
            </ul> :
            <div>
                <p>There are no open positions at this time.</p>
            </div>;
    }

    render() {
        return this.loading ? this.renderLoadingSpinner() : this.renderJobsList();
    }
}
