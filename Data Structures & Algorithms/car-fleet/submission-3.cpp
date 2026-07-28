class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {
        vector<pair<int,int>> cars;
        for (int i = 0; i < position.size(); i++) {
            cars.push_back({position[i], speed[i]});
        }

        sort(cars.rbegin(), cars.rend()); // sort by position descending

        int fleets = 0;
        double maxTime = 0;

        for (auto& p : cars) {
            double time = (double)(target - p.first) / p.second;
            if (time > maxTime) {
                fleets++;
                maxTime = time;
            }
        }

        return fleets;
    }
};
