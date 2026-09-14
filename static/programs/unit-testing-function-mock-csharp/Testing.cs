using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi;
using Pulumi.Testing;

class Mocks : IMocks
{
    public Task<(string? id, object state)> NewResourceAsync(MockResourceArgs args)
    {
        var outputs = ImmutableDictionary.CreateBuilder<string, object>();
        outputs.AddRange(args.Inputs);

        args.Id ??= $"{args.Name}_id";
        return Task.FromResult<(string? id, object state)>((args.Id, (object)outputs));
    }

    public Task<object> CallAsync(MockCallArgs args)
    {
        if (args.Token == "aws:ec2/getAmi:getAmi")
        {
            return Task.FromResult<object>(new Dictionary<string, object>
            {
                { "id", "ami-0eb1f3cdeeb8eed2a" },
                { "architecture", "x86_64" },
            });
        }

        return Task.FromResult((object)ImmutableDictionary<string, object>.Empty);
    }
}

public static class Testing
{
    public static Task<ImmutableArray<Resource>> RunAsync<T>() where T : Stack, new()
    {
        return Deployment.TestAsync<T>(new Mocks(), new TestOptions { IsPreview = false });
    }

    public static Task<T> GetValueAsync<T>(this Output<T> output)
    {
        var tcs = new TaskCompletionSource<T>();
        output.Apply(v =>
        {
            tcs.SetResult(v);
            return v;
        });
        return tcs.Task;
    }
}
