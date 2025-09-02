---
title: Start Building with Pulumi
meta_desc: Choose your cloud and language to begin building infrastructure as code with Pulumi
layout: start-now
no_on_this_page: true
---

<div class="container mx-auto px-6 py-12">
    <div class="text-center mb-12">
        <h1 class="text-4xl font-bold mb-4">Start Building with Pulumi</h1>
        <p class="text-xl text-gray-600">Choose your cloud and language to begin</p>
    </div>

    <!-- Choose Your Path Section -->
    <div class="mb-16">
        <h2 class="text-2xl font-semibold mb-8 text-center">Choose Your Path</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
            <a href="/docs/iac/get-started/" class="block p-6 bg-white rounded-lg shadow hover:shadow-lg transition-shadow border border-gray-200">
                <h3 class="text-xl font-semibold mb-3">
                    <i class="fas fa-rocket text-blue-500 mr-2"></i>
                    I'm new to Pulumi
                </h3>
                <p class="text-gray-600">Start with our beginner-friendly tutorial that explains core concepts and walks you through your first deployment.</p>
            </a>
            <a href="/docs/iac/get-started/terraform/" class="block p-6 bg-white rounded-lg shadow hover:shadow-lg transition-shadow border border-gray-200">
                <h3 class="text-xl font-semibold mb-3">
                    <i class="fas fa-exchange-alt text-green-500 mr-2"></i>
                    I'm migrating from Terraform
                </h3>
                <p class="text-gray-600">Learn how to import existing Terraform resources and convert HCL to Pulumi code in your preferred language.</p>
            </a>
            <a href="/templates/" class="block p-6 bg-white rounded-lg shadow hover:shadow-lg transition-shadow border border-gray-200">
                <h3 class="text-xl font-semibold mb-3">
                    <i class="fas fa-cubes text-purple-500 mr-2"></i>
                    I want to explore templates
                </h3>
                <p class="text-gray-600">Browse our collection of production-ready templates for common architectures and use cases.</p>
            </a>
        </div>
    </div>

    <!-- Choose Your Cloud & Language Section -->
    <div class="mb-16">
        <h2 class="text-2xl font-semibold mb-8 text-center">Choose Your Cloud & Language</h2>
        <p class="text-center text-gray-600 mb-8">Select your preferred cloud provider and programming language to get started with a tailored guide.</p>
        
        <!-- Cloud Provider Tabs -->
        <pulumi-chooser type="cloud" options="aws,azure,gcp,kubernetes">
            <!-- AWS -->
            <pulumi-choosable type="cloud" value="aws">
                <div class="mt-8">
                    <h3 class="text-xl font-semibold mb-6 text-center">AWS with Your Preferred Language</h3>
                    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
                        <a href="/start-now/aws-typescript/" class="text-center p-4 bg-blue-50 rounded-lg hover:bg-blue-100 transition-colors">
                            <img src="/logos/tech/typescript.svg" alt="TypeScript" class="h-12 mx-auto mb-2">
                            <span class="block font-medium">TypeScript</span>
                        </a>
                        <a href="/start-now/aws-python/" class="text-center p-4 bg-blue-50 rounded-lg hover:bg-blue-100 transition-colors">
                            <img src="/logos/tech/python.svg" alt="Python" class="h-12 mx-auto mb-2">
                            <span class="block font-medium">Python</span>
                        </a>
                        <a href="/start-now/aws-go/" class="text-center p-4 bg-blue-50 rounded-lg hover:bg-blue-100 transition-colors">
                            <img src="/logos/tech/go.svg" alt="Go" class="h-12 mx-auto mb-2">
                            <span class="block font-medium">Go</span>
                        </a>
                        <a href="/start-now/aws-csharp/" class="text-center p-4 bg-blue-50 rounded-lg hover:bg-blue-100 transition-colors">
                            <img src="/logos/tech/dotnet.svg" alt="C#" class="h-12 mx-auto mb-2">
                            <span class="block font-medium">C#</span>
                        </a>
                        <a href="/start-now/aws-java/" class="text-center p-4 bg-blue-50 rounded-lg hover:bg-blue-100 transition-colors">
                            <img src="/logos/tech/java.svg" alt="Java" class="h-12 mx-auto mb-2">
                            <span class="block font-medium">Java</span>
                        </a>
                        <a href="/start-now/aws-yaml/" class="text-center p-4 bg-blue-50 rounded-lg hover:bg-blue-100 transition-colors">
                            <img src="/logos/tech/yaml.svg" alt="YAML" class="h-12 mx-auto mb-2">
                            <span class="block font-medium">YAML</span>
                        </a>
                    </div>
                </div>
            </pulumi-choosable>
            
            <!-- Azure -->
            <pulumi-choosable type="cloud" value="azure">
                <div class="mt-8">
                    <h3 class="text-xl font-semibold mb-6 text-center">Azure with Your Preferred Language</h3>
                    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
                        <a href="/start-now/azure-typescript/" class="text-center p-4 bg-blue-50 rounded-lg hover:bg-blue-100 transition-colors">
                            <img src="/logos/tech/typescript.svg" alt="TypeScript" class="h-12 mx-auto mb-2">
                            <span class="block font-medium">TypeScript</span>
                        </a>
                        <a href="/start-now/azure-python/" class="text-center p-4 bg-blue-50 rounded-lg hover:bg-blue-100 transition-colors">
                            <img src="/logos/tech/python.svg" alt="Python" class="h-12 mx-auto mb-2">
                            <span class="block font-medium">Python</span>
                        </a>
                        <a href="/start-now/azure-go/" class="text-center p-4 bg-blue-50 rounded-lg hover:bg-blue-100 transition-colors">
                            <img src="/logos/tech/go.svg" alt="Go" class="h-12 mx-auto mb-2">
                            <span class="block font-medium">Go</span>
                        </a>
                        <a href="/start-now/azure-csharp/" class="text-center p-4 bg-blue-50 rounded-lg hover:bg-blue-100 transition-colors">
                            <img src="/logos/tech/dotnet.svg" alt="C#" class="h-12 mx-auto mb-2">
                            <span class="block font-medium">C#</span>
                        </a>
                        <a href="/start-now/azure-java/" class="text-center p-4 bg-blue-50 rounded-lg hover:bg-blue-100 transition-colors">
                            <img src="/logos/tech/java.svg" alt="Java" class="h-12 mx-auto mb-2">
                            <span class="block font-medium">Java</span>
                        </a>
                        <a href="/start-now/azure-yaml/" class="text-center p-4 bg-blue-50 rounded-lg hover:bg-blue-100 transition-colors">
                            <img src="/logos/tech/yaml.svg" alt="YAML" class="h-12 mx-auto mb-2">
                            <span class="block font-medium">YAML</span>
                        </a>
                    </div>
                </div>
            </pulumi-choosable>
            
            <!-- Google Cloud -->
            <pulumi-choosable type="cloud" value="gcp">
                <div class="mt-8">
                    <h3 class="text-xl font-semibold mb-6 text-center">Google Cloud with Your Preferred Language</h3>
                    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
                        <a href="/start-now/gcp-typescript/" class="text-center p-4 bg-blue-50 rounded-lg hover:bg-blue-100 transition-colors">
                            <img src="/logos/tech/typescript.svg" alt="TypeScript" class="h-12 mx-auto mb-2">
                            <span class="block font-medium">TypeScript</span>
                        </a>
                        <a href="/start-now/gcp-python/" class="text-center p-4 bg-blue-50 rounded-lg hover:bg-blue-100 transition-colors">
                            <img src="/logos/tech/python.svg" alt="Python" class="h-12 mx-auto mb-2">
                            <span class="block font-medium">Python</span>
                        </a>
                        <a href="/start-now/gcp-go/" class="text-center p-4 bg-blue-50 rounded-lg hover:bg-blue-100 transition-colors">
                            <img src="/logos/tech/go.svg" alt="Go" class="h-12 mx-auto mb-2">
                            <span class="block font-medium">Go</span>
                        </a>
                        <a href="/start-now/gcp-csharp/" class="text-center p-4 bg-blue-50 rounded-lg hover:bg-blue-100 transition-colors">
                            <img src="/logos/tech/dotnet.svg" alt="C#" class="h-12 mx-auto mb-2">
                            <span class="block font-medium">C#</span>
                        </a>
                        <a href="/start-now/gcp-java/" class="text-center p-4 bg-blue-50 rounded-lg hover:bg-blue-100 transition-colors">
                            <img src="/logos/tech/java.svg" alt="Java" class="h-12 mx-auto mb-2">
                            <span class="block font-medium">Java</span>
                        </a>
                        <a href="/start-now/gcp-yaml/" class="text-center p-4 bg-blue-50 rounded-lg hover:bg-blue-100 transition-colors">
                            <img src="/logos/tech/yaml.svg" alt="YAML" class="h-12 mx-auto mb-2">
                            <span class="block font-medium">YAML</span>
                        </a>
                    </div>
                </div>
            </pulumi-choosable>
            
            <!-- Kubernetes -->
            <pulumi-choosable type="cloud" value="kubernetes">
                <div class="mt-8">
                    <h3 class="text-xl font-semibold mb-6 text-center">Kubernetes with Your Preferred Language</h3>
                    <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
                        <a href="/start-now/kubernetes-typescript/" class="text-center p-4 bg-blue-50 rounded-lg hover:bg-blue-100 transition-colors">
                            <img src="/logos/tech/typescript.svg" alt="TypeScript" class="h-12 mx-auto mb-2">
                            <span class="block font-medium">TypeScript</span>
                        </a>
                        <a href="/start-now/kubernetes-python/" class="text-center p-4 bg-blue-50 rounded-lg hover:bg-blue-100 transition-colors">
                            <img src="/logos/tech/python.svg" alt="Python" class="h-12 mx-auto mb-2">
                            <span class="block font-medium">Python</span>
                        </a>
                        <a href="/start-now/kubernetes-go/" class="text-center p-4 bg-blue-50 rounded-lg hover:bg-blue-100 transition-colors">
                            <img src="/logos/tech/go.svg" alt="Go" class="h-12 mx-auto mb-2">
                            <span class="block font-medium">Go</span>
                        </a>
                        <a href="/start-now/kubernetes-csharp/" class="text-center p-4 bg-blue-50 rounded-lg hover:bg-blue-100 transition-colors">
                            <img src="/logos/tech/dotnet.svg" alt="C#" class="h-12 mx-auto mb-2">
                            <span class="block font-medium">C#</span>
                        </a>
                        <a href="/start-now/kubernetes-java/" class="text-center p-4 bg-blue-50 rounded-lg hover:bg-blue-100 transition-colors">
                            <img src="/logos/tech/java.svg" alt="Java" class="h-12 mx-auto mb-2">
                            <span class="block font-medium">Java</span>
                        </a>
                        <a href="/start-now/kubernetes-yaml/" class="text-center p-4 bg-blue-50 rounded-lg hover:bg-blue-100 transition-colors">
                            <img src="/logos/tech/yaml.svg" alt="YAML" class="h-12 mx-auto mb-2">
                            <span class="block font-medium">YAML</span>
                        </a>
                    </div>
                </div>
            </pulumi-choosable>
        </pulumi-chooser>
    </div>

    <!-- Popular Starting Points -->
    <div class="mb-16">
        <h2 class="text-2xl font-semibold mb-8 text-center">Popular Starting Points</h2>
        <p class="text-center text-gray-600 mb-8">Build something real with these engaging examples</p>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <a href="/templates/container-service/aws/" class="block p-6 bg-white rounded-lg shadow hover:shadow-lg transition-shadow border border-gray-200">
                <i class="fas fa-ship text-3xl text-blue-500 mb-4"></i>
                <h3 class="text-lg font-semibold mb-2">Deploy a Containerized Web App</h3>
                <p class="text-gray-600 text-sm">Build and deploy a containerized application with auto-scaling and load balancing.</p>
            </a>
            <a href="/templates/kubernetes/aws/" class="block p-6 bg-white rounded-lg shadow hover:shadow-lg transition-shadow border border-gray-200">
                <i class="fas fa-dharmachakra text-3xl text-green-500 mb-4"></i>
                <h3 class="text-lg font-semibold mb-2">Set up a Kubernetes Cluster</h3>
                <p class="text-gray-600 text-sm">Create a production-ready Kubernetes cluster with monitoring and ingress.</p>
            </a>
            <a href="/templates/serverless-application/aws/" class="block p-6 bg-white rounded-lg shadow hover:shadow-lg transition-shadow border border-gray-200">
                <i class="fas fa-bolt text-3xl text-yellow-500 mb-4"></i>
                <h3 class="text-lg font-semibold mb-2">Build a Serverless API</h3>
                <p class="text-gray-600 text-sm">Create a REST API using serverless functions with a database backend.</p>
            </a>
            <a href="/templates/static-website/aws/" class="block p-6 bg-white rounded-lg shadow hover:shadow-lg transition-shadow border border-gray-200">
                <i class="fas fa-globe text-3xl text-purple-500 mb-4"></i>
                <h3 class="text-lg font-semibold mb-2">Create a Static Website with CDN</h3>
                <p class="text-gray-600 text-sm">Deploy a static website with global CDN distribution and HTTPS.</p>
            </a>
        </div>
    </div>

    <!-- Learning Resources -->
    <div class="bg-gray-50 rounded-lg p-8">
        <h2 class="text-2xl font-semibold mb-8 text-center">Learning Resources</h2>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
            <a href="/learn/" class="flex items-center space-x-3 hover:text-blue-600">
                <i class="fas fa-graduation-cap text-xl"></i>
                <span>Interactive Tutorials</span>
            </a>
            <a href="https://www.youtube.com/c/PulumiTV" class="flex items-center space-x-3 hover:text-blue-600">
                <i class="fas fa-video text-xl"></i>
                <span>Video Walkthroughs</span>
            </a>
            <a href="/templates/" class="flex items-center space-x-3 hover:text-blue-600">
                <i class="fas fa-project-diagram text-xl"></i>
                <span>Architecture Templates</span>
            </a>
            <a href="/community/" class="flex items-center space-x-3 hover:text-blue-600">
                <i class="fas fa-users text-xl"></i>
                <span>Community Examples</span>
            </a>
        </div>
    </div>
</div>