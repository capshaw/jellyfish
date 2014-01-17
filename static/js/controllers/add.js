'use strict';

angular.module('app')
    .controller('AddCtrl', function ($scope, $http, apiService, $location,
        $routeParams) {

        apiService.getUser().then(function () {
            // Great, they're logged in.
        }, function (data){
            $location.path('/login');
        });

        // When 'add,' content is empty to begin with. Otherwise, load the
        // content from the backend.
        $scope.content = '';
        if ('entryId' in $routeParams) {
            $scope.entryId = $routeParams.entryId;
            apiService.getEntry($scope.entryId).then(function(data){
                $scope.entry = data;
                $scope.edit = true;
            });
        }

        var source_textarea = document.getElementById('source');
        tabOverride.set(source_textarea);

        var converter = new Showdown.converter();

        $scope.markdown = function (input) {
            return converter.makeHtml(input);
        };

        $scope.saveEntry = function () {
            if ($scope.edit) {
                $scope.updateEntry();
            } else {
                $scope.postEntry();
            }
        };

        $scope.postEntry = function () {
            apiService.postEntry($scope.entry.content).then(function(){
                $location.path('/home');
            });
        };

        $scope.updateEntry = function () {
            apiService.updateEntry($scope.entryId, $scope.entry.content).then(
                function(){
                $location.path('/home');
            })
        };
    });