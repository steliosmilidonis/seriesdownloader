#!/usr/bin/perl
use Expect;

use LWP::UserAgent;

my $url = 'http://192.168.0.29:8888/api/login';
my $json = '{"username": "admin", "password": "openmediavault"}';

my $ua = new LWP::UserAgent();
$response = $ua->post($url, Content => $json);

if ( $response->is_success() ) {
    print("SUCCESSFUL LOGIN!\n");
}
else {
    print("ERROR: " . $response->status_line());
}

my $url2 = 'http://192.168.0.29:8888/api/addPackage';
my $path = "http://uploaded.net/file/lwztghht/F-F-2015-C4.rar";
my $json2 = '{"name": "series", "links": /[\"http://uploaded.net/file/lwztghht/F-F-2015-C4.rar\"]"}';
my $ua2 = new LWP::UserAgent();

$response2 = $ua2->post($url2, Content => $json2);

if ( $response2->is_success() ) {
    print("SUCCESSFUL LOGIN!\n");
}
else {
    print("ERROR: " . $response->status_line());
}