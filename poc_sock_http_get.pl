use IO::Socket::Socks::Wrapper (
    Net::HTTP => {
        ProxyAddr => 'localhost',
        ProxyPort => 9050,
        SocksVersion => 4
    },
    Net::HTTPS => {
        ProxyAddr => 'localhost',
        ProxyPort => 9050,
        SocksVersion => 5
    }
);
use LWP;


my $lwp = LWP::UserAgent->new( agent => q{Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; YPC 3.2.0; .NET 
CLR 1.1.4322)},);

my $resp = $lwp->get('https://www.google.cl/search?q=site%3Acl+%2B+filetype%3Atxt&oq=site%3Acl+%2B+filetype%3Atxt');
print $resp->content, "\n";
