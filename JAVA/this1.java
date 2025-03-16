
import java.util.*;

public class this1{
    public static void main(string args[])
    {
        pwr x=newpwr(6.0,3);
        pwr y=newpwr(2.5,1);
        pwr z=newpwr(5.7,0);

        system.out.println(x.b+"raised to the"+x.e+"power is"+x.get_pwr());
        system.out.println(y.b+"raised to the"+y.e+"power is"+y.get_pwr());
        system.out.println(z.b+"raised to the"+z.e+"power is"+z.get_pwr());

    }
}
class pwr
{
    double b;
    int e;
    double val;

    pwr()
    {
        this.b=base;
        this.e=exp;
        this.val=1;
        if(exp==0)
        {
            return;

        }
        for(;exp>0;exp--)
        {
            this.val*=base;
        }
    }
    double get_pwr()
    {
        return this.val;
    }
    
}