angular.module('notesApp')
    .controller('AddCtrl', function ($scope, $timeout, $http) {

        var converter = new Showdown.converter();

        $scope.maxWords = 100;
        
        $scope.numWords = function (block) {
            if (block == null) {
                return 0;
            }
            return block.split(" ").length;
        }

        $scope.add = function () {
            var data = {
                title: $scope.title,
                content: $scope.content
            }
            $http({method: 'POST', url: '/notes/', data: data}).
              success(function(data, status, headers, config) {
                // this callback will be called asynchronously
                // when the response is available
              }).
              error(function(data, status, headers, config) {
                // called asynchronously if an error occurs
                // or server returns response with an error status.
              });
        };

        $scope.delete = function (id) {
            $http({method: 'DELETE', url: '/notes/' + id}).
              success(function(data, status, headers, config) {
                // this callback will be called asynchronously
                // when the response is available
              }).
              error(function(data, status, headers, config) {
                // called asynchronously if an error occurs
                // or server returns response with an error status.
              });
        };

        $scope.markdown = function (input) {
            return converter.makeHtml(input);
        }
    });