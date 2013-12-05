angular.module('notesApp')
    .controller('NotesCtrl', function ($scope, $timeout, $http) {

        var converter = new Showdown.converter();

        $scope.parseDate = function (date) {
            return new Date(Date.parse(date)).toString();
        }

        $http({method: 'GET', url: '/notes/'}).
          success(function(data, status, headers, config) {
            $scope.notes = data.notes;
          }).
          error(function(data, status, headers, config) {
            // called asynchronously if an error occurs
            // or server returns response with an error status.
          });

        $scope.markdown = function (input) {
            return converter.makeHtml(input);
        }
    });