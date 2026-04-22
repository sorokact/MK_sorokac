function[XB,YB] = boundary(R, uk, vk, u0, proj, ub, vb)
    %Draw boundary lines (cutting edges)
    
    %Transform to oblique aspect
    [sb, db] = uvTosd(ub, vb, uk, vk);
    
    %Project points
    [XB, YB] = proj(R, sb, db, u0);
end