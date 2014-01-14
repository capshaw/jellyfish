'use strict';

angular.module('app')
    .controller('HomeCtrl', function ($scope, apiService) {
        apiService.getEntries().then(function(data){
            $scope.entries = data.entries;
        });
    });