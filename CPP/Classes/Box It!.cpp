class Box
{
    long long l,b,h;

public:
    Box(){l = 0;b = 0;h = 0;}
    Box(int l,int b,int h){this->l = l;this->b = b;this->h = h;}
    Box(Box& box){l = box.l;b = box.b;h = box.h;}

    int getLength(){return l;}
    int getBreadth(){return b;}
    int getHeight(){return h;}
    long long CalculateVolume(){return l*b*h;}
    bool operator<(Box& box)
    {
        if(l<box.l){return true;}
        else if((b<box.b)&&(l == box.l)){return true;}
        else if((h<box.h)&&(b == box.b)&&(l == box.l)){return true;}
        else{return false;}
    }
    friend ostream& operator<<(ostream& out, Box& B)
    {
        out << B.l << " " << B.b << " " << B.h;
        return out;
    }
};

