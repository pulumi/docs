// PulumiEvent contains the data for a Pulumi event listing.
export interface PulumiEvent {
    archetype: "event" | "webinar";
    title: string;
    type: string[];
    description: string;
    startDate: Date;
    registrationUrl: string;
    external: boolean;
    imageSrc: string;
}

// PulumiRawWebinar contains the information for a webinar create in the
// webinars directory, i.e. `hugo new --kind webinar`.
export interface PulumiRawWebinar {
    draft: boolean;
    external: boolean;
    featured: boolean;
    gated: boolean;
    hero: {
        image: string;
        title: string;
    }
    iscjklanguage: boolean;
    main: {
        datetime: string;
        description: string;
        duration: string;
        learn: string[];
        presenters: { name: string; role: string; }[];
        sortable_date: string;
        title: string;
        youtube_url: string;
    };
    meta_desc: string;
    pre_recorded: boolean;
    preview_image: string;
    pulumi_tv: boolean;
    title: string;
    type: string;
    unlisted: boolean;
    url_slug: string;
}

// PulumiRawEvent contains the information for an event created in the
// events directory, i.e. `hugo new --kind event`.
export interface PulumiRawEvent {
    block_external_search_index: boolean;
    draft: boolean;
    event: {
        description: string;
        end_date: Date;
        location: string;
        registration_url: string;
        start_date: Date;
        type: string;
    }
    iscjklanguage: boolean;
    redirect_to: string;
    url_slug: string;
    title: string;
}
