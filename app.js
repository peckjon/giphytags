var app = angular.module('giphytags',[]);

app.controller('giphytagsController', function($scope, $http) {

    $scope.result = '';

    $scope.getTags = function() {
        $scope.result = 'Loading...';
        var re = /.*\/media\/(.*)\/giphy.gif/;
        var match = re.exec($scope.giphyurl);
        if(!match || match.length<1) {
            return $scope.result = "That doesn't appear to be a Giphy image URL";
        }
        var id = match[1];
        $http({method:'POST',url:'/json/giphytags',data:{id:id}}).then(
            function(response) {
                $scope.result = response.data;
            },
            function(response) {
                $scope.result = response.statusText;
            }

        );
    };

});