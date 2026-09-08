using System.Linq;
using System.Threading.Tasks;
using NUnit.Framework;

[TestFixture]
public class AmiTests
{
    [Test]
    public async Task InstanceUsesLookedUpAmi()
    {
        var resources = await Testing.RunAsync<WebserverStack>();

        var stack = resources.OfType<WebserverStack>().First();
        var ami = await stack.Server.Ami.GetValueAsync();

        Assert.That(ami, Is.EqualTo("ami-0eb1f3cdeeb8eed2a"));
    }
}
