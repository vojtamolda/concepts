@0x8ab367a17eca915a;

struct Temperature {
    value @0 :Float64;
    unit @1 :Unit;

    enum Unit {
        k @0;
        f @1;
        c @2;
    }
}
